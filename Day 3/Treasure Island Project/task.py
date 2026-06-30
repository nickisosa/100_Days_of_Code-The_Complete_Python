ascii_art = r"""
                    .,,.    ..
                  z$$$$$b c$$$L
               ,,$$$$$$$F,,"?$$                .,,,
          ,c" z$$$$$$$$",$$$c`F .          ,c$$$$,.
         ,$" d$$$$$$P",d$$$$$b'F3$ccc,,cc$$$$$$$$$$$c
        4$F 4$$$PF",c$$$?$$$$" $c$$$$$$$$$$$$$$$$$$$".
        $PL 4$$zc$'$$PLd$$$$$P 3$$$$$$$$$$$$$$$$$$$$$$F
        $ L '$$$$P,$$$"" d$$ : ?$$$$$$$$$$$$$$$$$$$$$P
         J$L d$P",$$$L,-,$$$b;h $$$$$$$$$$$$$$$$$$$P",c
         ?$$.$ '$$$$$$$$$$$$c;F $$$$$$$$$$$$$$$$?5,c$$$
         `$$'."?,"L$$$$$$$$ :/,d$$$$$L"$$$$$$$$$$$$$$$"
          "$b"$cc,"$$$$$$$$cr,$$$$$$$?b,"?$$$$$$$$$$P"
            "?$$$$c`$$$bK""=d$$P??",r= ??$c,.",,
 `L c ,         F?$-"$$F <!'; nnMM",;<!!; ?$$$$$P"
 k`b$,F          "";;" <!!' ,MMMM";!!!!' - $$P"
  3$Fb$    =nnnnd>`',;!!>',nMMMM ;!!!!><$$c,
   "$ $   <>"MMMMMn'''' ,nMMMM  <!!!!! d$$$$$c,
    $c"    `-,`TC)MMMMMMMMMMMM >`!!!!!;,"?$$$$$bc
   ,$$    ,cb,`<, )MMMMMMMMMMM !;,````     ""C3$$$,
   $$$F ,c$$$$P'<> )L.,cc,,"TMe`!!!!!!   ,c$$$$$$$$P
  <$$$$ $$$$F  ``   b,`C77?9hcc,,,,,ccd$$$$$$PF""
  3$$$$ $$P"        `4n,""??"".,,,       .,,xn,,.
  4$$$$cP"            `"4MMMMMMMP",==~",;;,.  -=MMMMMMMMMMM=
   $$P"                    ""_r='".df:!!!!!!!!!;, ""~=<
   `                      ,xP" xMMMMM <!!!!!!!!!!!>
                     _,eM"",dfJMMMMMMM.`!!!!!!!!!!!!;
                  ,nMMP",dMMMLMMMMMMMMMe`!!!!!!!!!!!!>
              ,eMMMMP",MMMMMMMMMMMMMMMMMe`!!!!!!!!!!!!>
            eMMMMMM",dMMMMMMMMMMMMMMMMMMMr`!!!!!!!!!!!!
         ,dMMMMMMP',MMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!!!
       ,dMMMMMMMP dMMMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!!!
     ,MMMMMMMMM" dMMMMMMMMMMMMMMMMMMMMMMMM !!!!!!!!!!!>!
   eMMMMMMMMMMP MMMMMMMMMMMMMMMMMMMMMMMMMP !!!!!!!!!!!;!
 eMMMMMMMMMMMM dMMMMMMMMMMMMMMMMMMMMMMMMM ;!!!!!!!!!' !'
"4MMMMMMMMMMM'uMMMMMMMMMMMMMMMMMMMMMMMMM> !!!!!!!!!',!!
;!> ;,"MMMMM>;MMMMMMMMMMMMMMMMMMMMMMMMMM <!!!!!!!' ,!!'
!! <!!>,"4MM ,c ;;;;,.""TMMMMMMMMMMMMMM>;!!!!!!' ,!!',
! <!!!!!!:." " <!!!!!!!!!:.""4MMMMMMMMM !!!!!! ,!!! ;!!,           . 4,
 <!!!!!!!!!!! <!!!!!!!!!!!!!!:..""TT";!!!! ,<!!!  !!!!>     .,zc$$$c",
;!!!!!!!!!!!';!!!!!!!!!!!!!!!!!!!!!!!!:!!! ,!!!!! ;>'!!!!!>"$$$$$P???L ",
!!!!!!!!!!!! !!!!!!!!!!!!!!!!!!!!!!!!!!'',!!!!!! ;!!> <!!!!>"$$"      ?P`b
!!!!!!!!!!! ,`'''!!!!!!!!!!!!!!!!!!!!',<!!!!!!!> !!!!> !!!!! ?         -$E
!!!!!!!!!!! <<',;;,``<!!!!!!!!!!!!!(;!!!!!!!!!!  !!!!! `!!!!!
`<!!!!!!!!!!> '``!!!>;`'!!!!!!!!!!!!!!!!!!!!!!!  !!!!!>'''`
   ``'''''!! `'dc,,zcc`;,``'!!!!!!!!!!!!!!!!!!!> !!!!!'
              ,$$$$$$$b`<!>;, ``''!!!!!!!!!!!!!> ```
             ,$$$$$$$$$F   ````       ```````
            ,$$$$$$$$"
            $$$$$$P"
          ,$$$$$P"
         ,$$$$"
"$c-, , '$$$F
 "$$c?,%,4$F
  `?$c"c'4"
     4c`b
       "

"""
print(ascii_art)
lucifer = r"""
           .'\   /`.
         .'.-.`-'.-.`.
    ..._:   .-. .-.   :_...
  .'    '-.(o ) (o ).-'    `.
 :  _    _ _`~(_)~`_ _    _  :
:  /:   ' .-=_   _=-. `   ;\  :
:   :|-.._  '     `  _..-|:   :
 :   `:| |`:-:-.-:-:'| |:'   :
  `.   `.| | | | | | |.'   .'
    `.   `-:_| | |_:-'   .'
 ---  `-._   ````    _.-'
          ``-------''

"""
# Welcome Statements
print("Welcome to Wonderland!")
print("You have entered a world of magic and mystery but you want to get out of here to get back to your world.")

print("You've fall through a shimmering, glitching mirror in your bedroom and land in a surreal clearing.\n "
      "In front of you are two winding paths: one lined with glowing blue mushrooms, the other with red glowing berries")

# Variables
choice1 = input('Do you want to go "left" or "right"?').lower()
# choice2 = input("Do you take the path with the blue mushrooms or the red berries? (Type 'blue' or 'red')")
win_art = "/^o^/"

# Conditions for the game
if choice1 == "left":
    choice2 = input('Do you take the path with the blue mushrooms or the red berries? (Type "blue" or "red")').lower()

    if choice2 == "blue":
        choice3 = input('Which door do you want to go through? "white", "brown" or "gold": ').lower()

        if choice3 == "gold":
            print(f"You win! You are on your way home! {win_art}")
        elif choice3 == "brown":
            print("Burned by fire. Game Over! 🔥")
        elif choice3 == "white":
            print("Eaten By Beasts Game Over! 🐻")
        else:
            print("Game Over!")
    else:
        print("Game Over! You'll Never Win. ❌")
else:
    print(f"Game Over! Try Again Another Time {lucifer}")

