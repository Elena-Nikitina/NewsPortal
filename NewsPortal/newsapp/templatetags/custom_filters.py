from django import template

register = template.Library()


@register.filter()
def censor(value):
   bad_words = ('редиска', 'баран', 'моргалы')

   if not isinstance(value, str):
      raise TypeError(f"unresolved type '{type(value)}' expected  type 'str'")

   for word in value.split():
      if word.lower().strip(',') in bad_words:
         value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
   return value






