import openai


with open("../openai.key") as f:
    openai.api_key = f.read().strip()

client = openai #.OpenAI()


if False:
    client.files.create(
    file=open("../data/train_set4.json", "rb"),
    purpose="fine-tune"
    )

if False:
    client.fine_tuning.jobs.create(
      training_file="file-NFd4goSEtrxhj4rAsjwGQu",
      #model="gpt-3.5-turbo"
      #model="gpt-4o-mini-2024-07-18"
      model="gpt-4o-2024-08-06"
    )


if False:
    completion = client.chat.completions.create(
      #model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
    #model="ft:gpt-3.5-turbo-0125:personal::9DxjYJle",
    #model= "ft:gpt-3.5-turbo-0125:personal::B1eKaRYa",
    model="ft:gpt-4o-2024-08-06:personal::B1iQ8l8h",

      #model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobnia"},
        {"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Sen jälkeen hevoset vietiin Mikkelimarkkinoille ja molemmat myytiin."}
      ]
    )

    print(completion.choices[0].message)

if False:
    completion = client.chat.completions.create(
    #model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
    #model="ft:gpt-3.5-turbo-0125:personal::9DxjYJle",
    #model= "ft:gpt-3.5-turbo-0125:personal::B1eKaRYa",
    #model="ft:gpt-4o-mini-2024-07-18:personal::B1hcGPmR",
    #model="ft:gpt-4o-2024-08-06:personal::B1iQ8l8h",
    model="ft:gpt-4o-2024-08-06:personal::B3poyXlC",

        #model="gpt-3.5-turbo",
      messages=[
        #{"role": "system", "content": "Hupulaanen is a factual chatbot that speaks also Finnish language dialect of South-Ostrobnia"},
        {"role": "system", "content":  "You translate standard Finnish sentences into the South Ostrobothnian dialect."},
        #{"role": "user", "content": "Ilmaise seuraava Etelä-Pohjanmaan murteella: Palavalla rakkaudella on surullinen loppu, tapasi isoisä vainaja sanoa."}
        {"role": "user", "content":  "Ilmaise seuraava Etelä-Pohjanmaan murteella: Meidän kylässä oli paljon hevoskauppiaita jotka olivat hevosen vaihtajia"}
      ]
    )

if True:
    completion = client.chat.completions.create(
    #model="ft:gpt-3.5-turbo-0125:personal::9Dsc8mIV",
    #model="ft:gpt-3.5-turbo-0125:personal::9DxjYJle",
    #model= "ft:gpt-3.5-turbo-0125:personal::B1eKaRYa",
    #model="ft:gpt-4o-mini-2024-07-18:personal::B1hcGPmR",
    #model="ft:gpt-4o-2024-08-06:personal::B1iQ8l8h",
    model="ft:gpt-4o-2024-08-06:personal::B3poyXlC",

        #model="gpt-3.5-turbo",
      messages=[
          {"role": "system", "content": "You are a storyteller who writes in the South Ostrobothnian dialect."},
          {"role": "user", "content": "Kirjoita tarina Etelä-Pohjanmaan murteella, joka perustuu seuraavaan otsikkoon: Hevoskauppiaat"}
          #{"role": "user", "content": "Kirjoita tarina Etelä-Pohjanmaan murteella, joka perustuu seuraavaan otsikkoon: Rintamaitovieroitus"}

      ]
    )

print(completion.choices[0].message)
