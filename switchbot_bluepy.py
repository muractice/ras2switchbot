import binascii
from bluepy.btle import Peripheral
import sys

mac_addr = "swithbotのmacアドレスを設定する"

p=Peripheral(mac_addr,"random")

hand_service = p.getServiceByUUID("cba20d00-224d-11e6-9fb8-0002a5d5c51b")

hand = hand_service.getCharacteristics("cba20002-224d-11e6-9fb8-0002a5d5c51b")[0]
hand.write(binascii.a2b_hex("570100"))
p.disconnect()

