pip install random-word

from random_word import RandomWords

r = RandomWords()
palabra = r.get_random_word()

# Validamos que la palabra sea válida (sin símbolos raros, espacios, etc.)
while not palabra.isalpha() or len(palabra) < 3 or len(palabra) > 10:
    palabra = r.get_random_word()

palabra = palabra.lower()
adivina_palabra = ['_'] * len(palabra)

print("Bienvenidos al juego de adivinar las palabras correctas!")

attempts = 10

while attempts > 0:
    print('\nPalabra actual: ' + ' '.join(adivina_palabra))
    guess = input('🔤 Adiviná una letra: ').lower()

    if guess in palabra:
        for i in range(len(palabra)):
            if palabra[i] == guess:
                adivina_palabra[i] = guess
        print('✅ ¡Buena letra!')
    else:
        attempts -= 1
        print(f'❌ Letra incorrecta. Intentos restantes: {attempts}')

    if '_' not in adivina_palabra:
        print('\n🎉 ¡Felicitaciones! Adivinaste la palabra: ' + palabra)
        break

if '_' in adivina_palabra:
    print('\n😢 ¡Te quedaste sin intentos! La palabra era: ' + palabra)
