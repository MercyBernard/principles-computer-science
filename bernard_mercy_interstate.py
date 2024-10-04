interstate_num = int(input('Please enter interstate number: '))

if interstate_num % 100 == 0:
    print(f'{interstate_num} is not a valid interstate highway number.')

else:
    if len(str(interstate_num)) == 3:
        if interstate_num % 10 == 0:
            primary = interstate_num % 100
            print(f'I-{interstate_num} is auxiliary, serving I-{primary}, going east/west.')
            
        else:
            primary = interstate_num % 100
            print(f'I-{interstate_num} is auxiliary, serving I-{primary}, going north/south.')

    elif len(str(interstate_num)) == 2:
        if interstate_num % 10 == 0:
           print(f'I-{interstate_num} is primary, going east/west.')

        else:
            print(f'I-{interstate_num} is primary, going north/south.')
        