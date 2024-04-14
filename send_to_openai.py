from openai import OpenAI
client = OpenAI()

if False:
    client.files.create(
    file=open("../data/train_set.json", "rb"),
    purpose="fine-tune"
    )

if False:
    client.fine_tuning.jobs.create(
      training_file="file-fDuhNiuP3FqwkiYiUrlqx1ou",
      model="gpt-3.5-turbo"
    )


if False:
    completion = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
      #model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Hupulaanen is a factual chatbot that is funny and speaks also Finnish language dialect of South-Ostrobnia"},
        {"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Sen jälkeen hevoset vietiin Mikkelimarkkinoille ja molemmat myytiin."}
      ]
    )

if True:
    completion = client.chat.completions.create(
      #model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobnia"},
        {"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Palavalla rakkaudella on surullinen loppu, tapasi isoisä vainaja sanoa."}
      ]
    )


print(completion.choices[0].message)
