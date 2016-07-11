import random, string
import sys

def generate_code(a, N = 10):
    b = [ord(ai.lower()) for ai in a]
    
    # Continued fractions to generate biyective R^N -> R
    c = 0
    for bi in b:
        c =+ (1./(bi+c))
    
    seed = int(c*1e15)
    random.seed(seed)
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


if __name__ == "__main__":
    try:
        input_code = sys.argv[1]
    except:
        input_code = '13AR10T32'

    code = generate_code(input_code)

    print 'Input:  ', input_code
    print 'Output: ', code

