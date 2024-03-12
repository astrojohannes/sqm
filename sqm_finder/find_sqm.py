import socket
import binascii

def find_sqm_le():
    # UDP broadcast settings
    broadcast_address = '255.255.255.255'
    port = 30718
    message = binascii.unhexlify('000000F6')
    buffer_size = 1024

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(30)

    try:
        # Send broadcast message
        sock.sendto(message, (broadcast_address, port))
        print("Broadcast message sent to {}:{}".format(broadcast_address, port))

        while True:
            # Listen for responses
            data, addr = sock.recvfrom(buffer_size)
            if data.startswith(binascii.unhexlify('000000F7')):
                mac_address = binascii.hexlify(data[24:30]).decode('utf-8')
                print("SQM-LE found at {} with MAC address: {}".format(addr[0], mac_address))
                break
    except socket.timeout:
        print("No response received. Timeout.")
    except Exception as e:
        print("An error occurred: {}".format(e))
    finally:
        sock.close()

if __name__ == '__main__':
    find_sqm_le()

