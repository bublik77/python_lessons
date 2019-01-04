# Q&A


1. Create EOSIO account
	- ./cleos.sh system newaccount --stake-net "100.0000 EOS" --stake-cpu "100.0000 EOS" --buy-ram-kbytes 4 <your accountr> <new account> <owner_pup_key> <active_pub_key>
2. Send EOS
	- ./cleos.sh transfer <your account>  <receiver account> "1.0000 EOS" "test memo text"
3. Get Balance
	- ./cleos.sh get currency balance eosio.token <account name>
4. List registered producers (-l <limit>)
	- ./cleos.sh get table eosio eosio producers -l 100
5. List staked/delegate
	- ./cleos.sh system listbw <account>
6. How init node first time 
	- Run ./start.sh --delete-all-blocks --genesis-json genesis.json in NODE folder
7. how can I check  REX balance
	- ./cleos.sh get table eosio eosio rexbal
	- ./cleos.sh get table eosio eosio rexpool
	- ./cleos.sh get table eosio eosio rexfund
	- ./cleos.sh get table eosio eosio cpuloan
	- ./cleos.sh get table eosio eosio netloan
	- ./cleos.sh get table eosio eosio delband
	- ./cleos.sh get table eosio eosio rexqueue
8. Deposit:
	- ./cleos.sh push action eosio deposit '{"owner":"<YOUR ACC>","amount":"<AMOUNT> EOS"}' -p <YOUR ACC>

9. Rent CPU
	- ./cleos.sh push action eosio rentcpu '{"from":"<YOUR ACC>","receiver":"<YOUR OR SOMEOENE ACC>","loan_payment":"<AMOUNT> EOS","loan_fund":"<AMOUNT> EOS"}' -p <YOUR ACC>

10. Buy REX
	- ./cleos.sh push action eosio buyrex '{"from":"<YOUR ACC>","amount":"<AMOUNT> EOS"}' -p testertester


