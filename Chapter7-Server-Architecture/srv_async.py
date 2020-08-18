# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:15:30 2020

@author: fikirsanat
"""

import select, zen_utils

def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event

def serve(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        # Socket closed: remove it from our data structures.

        """
            POLLIN: There is data to read
            POLLPRI: There is urgent data to read
            POLLOUT: Ready for output:writing will not block
            POLLERR: Error condition of some sort
            POLLHUP: Hung up
            POLLRDHUP: Stream socket peer closed connection,or shut down writing half of connection
            POLLNVAL:Invalid request:desriptor not open
        
        """
        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print('Client {} sent {} but then closed'.format(address, rb))
            elif sb:
                print('Client {} closed before we sent {}'.format(address, sb))
            else:
                print('Client {} closed socket normally'.format(address))
            poll_object.unregister(fd)
            del sockets[fd]

        # New socket: add it to our data structures.

        elif sock is listener:
            sock, address = sock.accept()
            print('Accepted connection from {}'.format(address))
            sock.setblocking(False)     # force socket.timeout if we blunder
            sockets[sock.fileno()] = sock
            addresses[sock] = address
            poll_object.register(sock, select.POLLIN)

        # Incoming data: keep receiving until we see the suffix.

        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:  # end-of-file
                sock.close()  # next poll() will POLLNVAL, and thus clean up
                continue
            data = bytes_received.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                bytes_to_send[sock] = zen_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data

        # Socket ready to send: keep sending until all bytes are delivered.

        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)

if __name__ == '__main__':
    address = zen_utils.parse_command_line('low-level async server')
    listener = zen_utils.create_srv_socket(address)
    serve(listener)
                
                
                
                
                
                
                
                
                
                
                
                
                
                