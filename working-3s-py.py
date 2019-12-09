from datetime import datetime
import zmq
import pyshark


context = zmq.Context.instance()
pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://127.0.0.1:1234")

cap = pyshark.LiveCapture(interface='eth1', bpf_filter='host 239.50.3.4')


def get_packets(pkt):
    try:
        timestamp = datetime.now()
        dst_addr = pkt.ip.dst
        frame_len = pkt.length
        pub_socket.send_pyobj(dict(x=[timestamp], y=[frame_len]))
    except AttributeError as e:
        pass


cap.apply_on_packets(get_packets) 