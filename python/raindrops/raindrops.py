def convert(number):
    pairs = { 3: 'Pling', 5: 'Plang', 7: 'Plong' }
    return ''.join([
        sound for factor, sound in pairs.items() if number % factor == 0
    ]) or str(number)
