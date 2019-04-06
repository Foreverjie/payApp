import os

from MyQR import myqr
#
# version, level, qr_name = myqr.run(
#     'https://github.com',
#     version=1,
#     level='H',
#     picture='test.jpg',
#     colorized=True,
#     contrast=1.0,
#     brightness=1.0,
#     save_name=None,
#     save_dir=os.getcwd()
# )


def get_qr(word, username, picture):
    myqr.run(
        word,
        version=1,
        level='H',
        picture=picture,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=username,
        save_dir='static/images/'
    )
