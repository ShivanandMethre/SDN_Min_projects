 # POX Controller: Port Monitoring with MAC Learning

# Blocks Telnet (port 23)

# Allows HTTP (port 80)

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

mac_to_port = {}

def _handle_ConnectionUp(event):
log.info("Switch connected")

def _handle_PacketIn(event):
packet = event.parsed
dpid = event.connection.dpid

```
if not packet.parsed:
    return

# Initialize table for switch
if dpid not in mac_to_port:
    mac_to_port[dpid] = {}

# Learn MAC address
mac_to_port[dpid][packet.src] = event.port

# Check destination MAC
if packet.dst in mac_to_port[dpid]:
    out_port = mac_to_port[dpid][packet.dst]
else:
    out_port = of.OFPP_FLOOD

# Check TCP packet
tcp = packet.find('tcp')
if tcp:
    if tcp.dstport == 23:
        log.info("Blocked Telnet (Port 23)")
        return   # Drop packet

    elif tcp.dstport == 80:
        log.info("Allowed HTTP (Port 80)")

# Forward packet
msg = of.ofp_packet_out()
msg.data = event.ofp
msg.in_port = event.port
msg.actions.append(of.ofp_action_output(port=out_port))

event.connection.send(msg)
```

def launch():
core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
log.info("Port Monitoring Controller Started")
