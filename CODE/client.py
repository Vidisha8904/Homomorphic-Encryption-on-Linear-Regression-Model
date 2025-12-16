import phe
import json

def keygen():
    public_key, private_key = phe.generate_paillier_keypair()
    keys={}
    keys['public_key'] = {'n': public_key.n}
    keys['private_key'] = {'p': private_key.p,'q':private_key.q}
    with open('keys.json', 'w') as file: 
    	json.dump(keys, file)  
    # return public_key, private_key

def getKeys():
	with open('keys.json', 'r') as file: 
		keys=json.load(file)
		pub_key=phe.PaillierPublicKey(n=int(keys['public_key']['n']))
		priv_key=phe.PaillierPrivateKey(pub_key,keys['private_key']['p'],keys['private_key']['q'])
		return pub_key, priv_key 

def serializeData(public_key, data):
	encrypted_data_list = [public_key.encrypt(x) for x in data]
	encrypted_data={}
	encrypted_data['public_key'] = {'n': public_key.n}
	encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in         encrypted_data_list]
	serialized = json.dumps(encrypted_data)
	return serialized
def loadAnswer():
    with open('answer.json', 'r') as file: 
        ans=json.load(file)
        answer=json.loads(ans)
        return answer
# keygen()
pub_key, priv_key= getKeys()
data = [
    depression_score,
    anxiety_score,
    substance_use_score,
    self_harm_risk_index,
    sleep_disorder_score,
    trauma_exposure_score,
    social_isolation_score,
    medication_adherence_score,
    work_burnout_index,
    suicidal_ideation_score
# ] = [12, 8, 5.5, 0.25, 6.0, 7.0, 5.0, 0.8, 6.5, 0.1]
# ]= [3, 1, 0.62, 0.023, 6.51, 3.66, 1.89, 0.695, 8.01, 0.178]
  ]=[27,10,5.15,0.759,1.82,6.19,7.91,0.231,1.82,0.267]

serializeData(pub_key, data)
datafile=serializeData(pub_key, data)
with open('data.json', 'w') as file: 
    json.dump(datafile, file)

answer=loadAnswer()
answer_key=phe.PaillierPublicKey(n=int(answer['pubkey']['n']))
answer1 = phe.EncryptedNumber(answer_key, int(answer['values'][0]), int(answer['values'][1]))
if (answer_key==pub_key):
    print(priv_key.decrypt(answer1))
else: 
    print("Keys do not match!")