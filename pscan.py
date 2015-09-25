#!/bin/python

import optparse
import socket


def connScan(tgtHost, tgtPort):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((tgtHost, tgtPort))
        s.send('yay\r\n')
        results = s.recv(100)
        print('/> {}:{}/tcp -> OPEN'.format(tgtHost, tgtPort))
        print('/> {]'.format(results))
        s.close()
    except:
        print('/> {}:{}/tcp -> CLOSED'.format(tgtHost, tgtPort))


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = socket.gethostbyname(tgtHost)
    except:
        print('Can not resolve Host.')
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIp)
        print('\n/> Scan Results for: ' + tgtName[0])
    except:
        print('\n/> Scan Result for: ' + tgtIp)
    socket.setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print('/> Scanning port:' + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parser = optparse.OptionParser('usage%prog '
                                   '-H <target host> -p <taget port>')
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string',
                      help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')

    if (tgtHost is None) or (tgtPorts[0] is None):
        print('/> No host or port(s) specified')
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
