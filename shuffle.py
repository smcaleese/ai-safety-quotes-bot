import json
import random

def main():
    with open('quotes.json') as f:
        quotes_list = json.load(f)['quotes']

    random.shuffle(quotes_list)

    shuffled_quotes = {'quotes': quotes_list}
    print(f'Number of quotes: {len(shuffled_quotes["quotes"])}')

    with open('quotes.json', 'w') as f:
        json.dump(shuffled_quotes, f, indent=4)

if __name__ == '__main__':
    main()
