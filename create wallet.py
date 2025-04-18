from thor_devkit import cry
from thor_devkit.cry import mnemonic
from thor_devkit.cry import hdnode
words = mnemonic.generate()
hd_node = cry.HDNode.from_mnemonic(words)
for i in range(0, 1):
   address='0x'+hd_node.derive(i).address().hex()
   privkey=hd_node.derive(i).private_key().hex()
# Print out everything
print('')
print('Your mnemonic words are    ' + str(words))
print('Your wallet private key is ' + str(privkey))
print('Your wallet address is     ' + str(address))
print('')