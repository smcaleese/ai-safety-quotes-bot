import json

def main():
    with open('quotes.json') as f:
        quotes_list = json.load(f)['quotes']

    count = 0
    for q in quotes_list:
        full_quote = q['quote'] + ' - ' + q['author']
        if len(full_quote) > 280:
            print(f'Quote too long: {len(full_quote)} / 280')
            print(full_quote)
            count += 1

    print(f'Number of quotes too long: {count}')

if __name__ == '__main__':
    main()
