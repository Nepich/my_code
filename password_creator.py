import string
import random

n,m = int(input()), int(input()) 
# n - количество требуемых паролей
# m - длинна каждого пароля

def generate_password(length):
    up = list(set(string.ascii_uppercase)-set('lI1oO0'))
    low = list(set(string.ascii_lowercase)-set('lI1oO0'))
    numbers = list(set(string.digits)-set('lI1oO0'))
    upper = [random.choice(up) for _ in range(random.randint(1,length-2))]
    lower = [random.choice(low) for _ in range(random.randint(1,length-len(upper)-1))]
    numbers = [random.choice(numbers) for _ in range(length-len(upper)-len(lower))]
    pasw = upper+lower+numbers
    random.shuffle(pasw)
    return ''.join(pasw)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


print(*generate_passwords(n,m), sep='\n')
