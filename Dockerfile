
# Python image dan foydalanish
FROM python:3.12

# Ishchi papkani yaratish
WORKDIR /app

# Talab qilingan paketlarni o'rnatish
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Kodlarni nusxalash
COPY . /app/

# Django va Telegram bot uchun o'zgaruvchilarni sozlash
ENV DJANGO_SETTINGS_MODULE=coder_movie_bot.settings

# Django va botni ishga tushirish
CMD ["sh", "-c", "gunicorn coder_movie_bot.wsgi:application --bind 0.0.0.0:8000 & python bot.py"]
