from django import template

register = template.Library()


@register.filter(name='odd')
def odd_nums(nums):
    return [num for num in nums if num % 2 == 0]
