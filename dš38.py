print('''
_                                       _   _            
| |                                     | | | |          
| |__   __ _ _ __ _ __ _   _ _ __   ___ | |_| |_ ___ _ __
| '_ \ / _` | '__| '__| | | | '_ \ / _ \| __| __/ _ \ '__|
| | | | (_| | |  | |  | |_| | |_) | (_) | |_| ||  __/ |  
|_| |_|\__,_|_|  |_|   \__, | .__/ \___/ \__|\__\___|_|  
                        __/ | |                          
                       |___/|_|                          
''')

print("""Vítejte v Bradavicích milí studenti!
Nyní se vypravíte do svých kolejí.""")
slytherin = input("Následovat spolužáky do své koleje Zmijozel? Napiště ano nebo ne. ")

if slytherin == "ano":
    print ("Právě jsi ve společenské místnosti Zmijozelu.")
    studying = input("Chceš se věnovat studiu na hodinu lektvarů s profesorem Snapem? Napište ano nebo ne. ").lower()
    if studying == "ano":
        print("Pořádně jsi se učil a určitě od Severuse dostaneš body pro svou kolej. 10 bodů pro Zmijozel.")
        gossips = (input("Potkáš Draca Malfoye. Chceš jít s Dracem pomlouvat Harryho Pottera? Napište ano nebo ne. ")).lower()
        if gossips == "ano":
            print("Na Draca jsi udělal dojem. Jsi v jeho vnitřním kruhu.")
        else:
            print("Učení ani drby tě nazajímají. Tak jdi spát.")
    else:
        print("Pokud se ti nechce učit, můžeš pomlouvat Harryho Pottera s Dracem.")


else:
    secret_chamber = input("Na kolej se ti nechce. Ocitáš se tady před vstupem do tajemné komnaty. Vstoupíš? Napište ano nebo ne. ").lower()
    if secret_chamber == "ano":
        print("Jsi ve středu tajemné komnaty a najednou proti tobě stojí hrozivý bazilišek.")
        basilisk = input("Máš dost odvahy se mu postavit? Napište ano nebo ne. ").lower()
        if basilisk == "ano":
            print("Použil jsi mocné kouzlo a baziliška zabil. Jsi hrdina. 100 bodů pro Zmijozel!!!")
        else:
            print("Bazilišek se na tebe podíval přes odraz ve vodě. Modli se, aby byl někdo další tak hloupý a lezl do tajemné komnaty.")
    else:
        print("Načapal tě Filch a ihned tě poslal zpět do své koleje.")