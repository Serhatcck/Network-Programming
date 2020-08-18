# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 16:01:01 2020

@author: fikirsanat
"""

import argparse, socket, time

aphorisms = {b'Beautiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}


#Bir cevap için bu sözlüğe güvenli bir arama yapmak için hızlı bir kısaltmadır
def get_answer(aphorism):
    """Return the string response to a particular Zen-of-Python aphorism."""
    time.sleep(0.0)  # increase to simulate an expensive operation
    return aphorisms.get(aphorism, b'Error: unknown aphorism.')


#Komut satırı argümanlarını okumak için orkat bir şema sağlar
def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


#Gelen bağlantıları almak için bir sunucunun ihtiyaç duyduğu dinleme TCP soketini oluşturur
def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}'.format(address))
    return listener


#Her bir bağlanan istemciyi print ile soketinin eylem için bir sonraki işleve temsil etmeden önce uyarır
def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        sock, address = listener.accept()
        print('Accepted connection from {}'.format(address))
        handle_conversation(sock, address)


# İstemci soketindeki herhangi bir sorunun programı çökertmesinin imkansız hale getirmek için tasarlanmış
#bir şekilde sınırsız sayıda istek-yanıt döngüsünü sarmaya yönelik bir hata yakalama ortamıdır
def handle_conversation(sock, address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_request(sock)
    except EOFError:
        print('Client socket to {} has closed'.format(address))
    except Exception as e:
        print('Client {} error: {}'.format(address, e))
    finally:
        sock.close()

#İstemciyle tek bir ileri-grei hareket gerçekleştirir,sorusunu okur ve ardından bir yanıt verir
def handle_request(sock):
    """Receive a single client request on `sock` and send the answer."""
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)


# Bölüm 5'te ana hatları ile açıklanana uygulamayı kullanarak çerçevelemeyi gerçekleştirir
#toplanan bayt dizgisi nihayet eksiksiz bir soru olaraka nitelendirilene kadar yuvanını recv()'e
#tekrarlanan çağrıları yapılır
def recv_until(sock, suffix):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('received {!r} then socket closed'.format(message))
        message += data
    return message