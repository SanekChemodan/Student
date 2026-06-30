from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")
print("Запускаем нейросеть")
generator=pipeline("text-generation", model="ai-forever/rugpt3small_based_on_gpt2")
print("Введи начало истории\n")
print("Для выхода напиши 'выход'\n")
while(True):
    user_input=input("Твое начало: ")
    if user_input.lower()=='Выход':
        break
    print("ИИ думает...")
    result=generator(user_input,max_length=150,num_return_sequences=1, truncation=True, do_sample=True, temperature=0.1, repetition_penalty=1.2)
    generated_text=result[0]['generated_text']
    print('Результат: \n')
    print(generated_text)