while True:
    while True:
        try:
            prime3ra = input('Escribe la primera palabra : ') 
            segunda = input('Escribe la segunda palabra : ')
            if prime3ra[-3::] == segunda[-3::]:
                print('Riman!')
            elif prime3ra[-2::] == segunda[-2::]:
                print('Riman un poco')
                print(prime3ra[-2::])
                print(segunda[-2::])
            else:
                print('No riman')
        except:
            print('porfavor solo palabras')
    break

