import pygame as pg
import sys, time, random
pg.font.init()
text_collection = [""]
random_num = random.randint(0,8)
text_1 =["Little alteration, except the growth of our dear children, has taken place since you left us. The blue lake and snow-clad mountains-they never change; and I think our placid home and our contented hearts are regulated by the same immutable laws. My trifling occupations take up my time and amuse me, and I am rewarded for any exertions by seeing none but happy, kind faces around me.", "You just typed a part of the book Frankenstein!"]
text_2 = ["Call me Ishmael. Some years ago-never mind how long precisely-having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation.", "You just typed part of the book Moby Dick!"]
text_3 = ["There was so much to read, for one thing, and so much fine health to be pulled down out of the young breath-giving air. I bought a dozen volumes on banking and credit and investment securities, and they stood on my shelf in red and gold like new money from the mint, promising to unfold the shining secrets that only Midas and Morgan and Maecenas knew.", "You just typed a part of the book The Great Gatsby"]
text_4 = ["The grey of the morning has passed, and the sun is high over the distant horizon, which seems jagged, whether with trees or hills I know not, for it is so far off that big things and little are mixed. I am not sleepy, and, as I am not to be called till I awake, naturally I write till sleep comes.", "You just typed a part of the book Dracula"]
text_5 = ["Pretty soon I wanted to smoke, and asked the widow to let me. But she wouldn't. She said it was a mean practice and wasn't clean, and I must try to not do it any more. That is just the way with some people. They get down on a thing when they don't know nothing about it.", "You Just typed a part of the book Adventures of Huckleberry Finne."]
text_6 = ["Tell me, Muse, of that man, so ready at need, who wandered far and wide, after he had sacked the sacred citadel of Troy, and many were the men whose towns he saw and whose mind he learnt, yea, and many the woes he suffered in his heart on the deep, striving to win his own life and the return of his company. Nay, but even so he saved not his company, though he desired it sore. For through the blindness of their own hearts they perished, fools, who devoured the oxen of Helios Hyperion: but the god took from them their day of returning. Of these things, goddess, daughter of Zeus, whencesoever thou hast heard thereof, declare thou even unto us.", "You just typed a part of the Odyssey"]
text_8 = ["Pierre was ungainly. Stout, about the average height, broad, with huge red hands; he did not know, as the saying is, how to enter a drawing room and still less how to leave one; that is, how to say something particularly agreeable before going away. Besides this he was absent-minded.", "You just typed a part of the book War and Peace"]
text_9 = ['"God order it as he may," said Sancho Panza, and helping him to rise got him up again on Rocinante, whose shoulder was half out; and then, discussing the late adventure, they followed the road to Puerto Lapice, for there, said Don Quixote, they could not fail to find adventures in abundance and variety, as it was a great thoroughfare."', "You just typed a part of the book Don Quixote"]
text_10 = ["Here is Edward Bear, coming downstairs now, bump, bump, bump, on the back of his head, behind Christopher Robin. It is, as far as he knows, the only way of coming downstairs, but sometimes he feels that there really is another way, if only he could stop bumping for a moment and think of it. And then he feels that perhaps there isn't. Anyhow, here he is at the bottom, and ready to be introduced to you. Winnie-the-Pooh.", "You just typed a part of the book Winnie-the-Pooh"]
text_collection= [text_1,text_2,text_3,text_4,text_5,text_6,text_8,text_9,text_10]
screen = pg.display.set_mode((1200, 600))
font = pg.font.Font(None, 32)
clock = pg.time.Clock()
color = pg.Color('dodgerblue2')
pg.display.set_caption("Word accuracy tester")
shift = False
seconds = 0
def main():
    global seconds
    text=""
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    print(text)
                    text = ''
                elif event.key == pg.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
        screen.fill((30, 30, 30))
        if text == text_collection[random_num][0][0:len(text)]:
            blit_text(screen, text, (20,250), font, "green")
        else: 
            blit_text(screen, text, (20,250), font, "red")
        blit_text(screen, text_collection[random_num][0], (20,20), font, "white")
        check_win(text)
        pg.display.flip()
        clock.tick(100)
def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0] 
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0] 
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height 
def check_win(typed_text):
    global seconds
    my_text = text_collection[random_num][0]
    win_text = text_collection[random_num][1]
    if typed_text == my_text:
        blit_text(screen, "Congragulations,"+win_text,(20,400), font, "green")
if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
        



# The passages used are in the public domain and were found at the these URL's:
# Frankenstein https://www.gutenberg.org/cache/epub/84/pg84-images.html
# Moby Dick https://www.gutenberg.org/cache/epub/2701/pg2701-images.html
# The Great Gatsy https://www.gutenberg.org/cache/epub/64317/pg64317-images.html
# Dracula https://www.gutenberg.org/cache/epub/345/pg345-images.html
# Adventures of Huckleberry Finn https://www.gutenberg.org/cache/epub/76/pg76-images.html
# The Odyssey https://www.gutenberg.org/cache/epub/1727/pg1727-images.html
# War and Peace https://www.gutenberg.org/cache/epub/2600/pg2600-images.html
# Don Quixote https://www.gutenberg.org/cache/epub/996/pg996-images.html
# Winnie-the-Pooh https://www.gutenberg.org/cache/epub/67098/pg67098-images.html
# Stack overflow URL's that I used code from are listed here:
# https://stackoverflow.com/questions/34402713/change-the-colour-of-python-text
# https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame
# https://stackoverflow.com/questions/66384680/how-to-detect-a-key-press-with-pygame
# https://stackoverflow.com/questions/46252905/on-screen-typing-in-pygame
