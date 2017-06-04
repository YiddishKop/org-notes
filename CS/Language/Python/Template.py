from string import Template

# 可以通过扩展Template这个子类，来定义自己的起始符
# 下面在调用Template生成模板的时候，需要用子类名字打头：MyTemplate
class MyTemplate(Template):
    delimiter = '#'


def Main():
    cart = []
    cart.append(dict(item="Coke", price=8, qty=2))
    cart.append(dict(item="Cake", price=12, qty=12))
    cart.append(dict(item="Fish", price=32, qty=4))

    # $qty $item $ price 就叫做 placeholder
    # 类似于 lazy-loading, 后面会填充数据。
    # placeholder -> template
    # dict -> template -> wanted data
    t = MyTemplate("#qty x #item = #price")
    w = MyTemplate("The #{qty} is so #{item}")
    total = 0
    print("Cart: ")
    for data in cart:
        print(t.substitute(data))
        print(w.substitute(data))
        total += data["price"]
    print("Total: " + str(total))


Main()
