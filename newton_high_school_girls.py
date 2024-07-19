def newton_high_school_girls():
    """
    how do I solve this question?

    ![imagme](https://media.discordapp.net/attachments/
    486844829209198613/1263648705811054663/image.
    png?ex=669b0010&is=6699ae90&hm=00a900e7b8a33837ba4
    a6e60c4a43e39756e40da4fb6abe52bc7257ada1d9e63&=&format=webp
    &quality=lossless)

    :return:
    """
    wins, losses, ties, games, cont = 8, 5, 0, 23, 8

    for i in range(10):
        wins += 1
        if wins / games > 0.50:
            print(wins - cont)
            break


newton_high_school_girls()
