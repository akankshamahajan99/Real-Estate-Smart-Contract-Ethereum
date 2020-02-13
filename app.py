from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

account_1 = "0xB8bbCfa6a9a8cfe4071eFED21F799ddBd9d4f4F0"
account_2 = "0xC211e1C6D9ef84ae36b25FB988F8E456ce9F1188"

private_key = "b21dd5818fb405784e59ec4970dfa6ed9477316dfaaf90657a8206a3071d22f0"

nonce = web3.eth.getTransactionCount(account_2)

tx = {
	'nonce': nonce,
	'to': account_1,
	'value':web3.toWei(16, 'ether'),
	'gas':200000,
	'gasPrice':web3.toWei('50', 'gwei')
}

signed_tx = web3.eth.account.signTransaction(tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(tx_hash)