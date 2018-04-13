# Cat 8.1 Function objects, exponential

objects compose a set, arrows compose a home set(can be illustrated as a point), set is object. it's a circle

![Function](https://s18.postimg.org/4wm05vi49/screenshot_40.png)

external hom-set and inner hom-set

because function is a object(set), so we can apply all the previous lectures theory to function
* unviersal construction, pattern
* product and coproduct
* ...

Cartesian product, we can generlize it to categorical product.

in order to define a function ,you must ifrst have a product(or ADT)

like if you want to define exponential, you must has a multiplication.

begin with universal construnction : 1. pattern 2. ranking


1. pattern
![pattern](https://s18.postimg.org/4l4jst45l/screenshot_41.png)
components: a,z,g,b
2. ranking
by unique morphism
go back to see the pattern and ranking of product and coproduct.

z' X a -> z X a

a product is a bifunctor, take two make 3nd one
                         alss  two function make 3nd one
go back to see bifunctor of product.

![ranking](https://s18.postimg.org/n0p0qaq0p/screenshot_42.png)


a unique morphism h exist, such that commute graph exsit -- 

g' = g * (h X id)

a=>b is fucntion object => is just  a symbol

![move further](https://s18.postimg.org/49rotz809/screenshot_43.png)

imperative language
f(x,y,z) is like f((x,y,z)) a functin one multi arg, is function on a tuple(of args)


g' = g * (h X id)
=>
g' = eval * (h X id)

one h ---> one g


??? 25:00 two way of thinking : 
1. g is from product(zXa) to b
2. one g for one h

then,

h:: z->(a->b)
g:: (z,a)->b

g and h are equalent.

it's something about curry, h is the curry version of g

curry:: ((a, b)->c) -> (a ->(b->c))
curry f = lambda  a -> (lamb b -> f(a,b))

uncurry:
![uncurry](https://s18.postimg.org/mqm3kwb4p/screenshot_44.png)


in haskell:
arrow -> will associate with right
function call f a b, will associate with left

### exponential
in Cat people call function object exponential, `a->b` is `b^a`

Bool->Int for 1 function , he can ONLY get 2 Int, one for true, one fro false;

if refer to type, from Bool to Int, **the number of functions** is just decided by Int --- like some reverse procession ,from return type to input type

Int X Int, a cartesian product.


![exponential of function](https://s18.postimg.org/o6xm2rj3t/screenshot_45.png)

it shows you connection between product and function type---exponential, iterative product gives you exponential.


Cartesian closed category --- CCC --- has terminal object, 
1. object^0 = terminal object
2. object^1 = object itself
3. object^n = exponential

Bi-Cartesian closed category --- BCCC


we have seen that , 
* the ADT using product gives you a monoid
* the ADT using coproduct gives you a another monoid
* the ADT using initial object(void) gives you a monoid
* the ADT using terminal object(unit) gives you a monoid
TODO * the ADT using exponential gives you a monoid

if we combine them, it will gives you a semi-ring


If we add exponential to it:

![many kinds of exponential](https://s18.postimg.org/oarfj2m15/screenshot_46.png)

# Cat 8.2 Type algebra, Curry-Howard-Lambek isomorphism

## Type algebra
![expression1](https://s9.postimg.org/wn51f6yxb/screenshot_47.png)
Either b c -> a
you will need a case match to implement this function


![expression2](https://s9.postimg.org/gowbp425b/screenshot_48.png)
It's something curry and uncurry


![expression3](https://s9.postimg.org/brir3ppsv/screenshot_49.png)

all these definition two side of "=", can replace each other.

like:

``` scala
def curryFn(b:Int)(c:String):Double = def uncurryFn(c:String): Int=>Double
//(b,c)->a = a^(b*c) = (a^b)^c = c ->(b->a)
```


## Curry-Howard-Lambek
all these stuff also can be used in logic area. This is the basis of famous curry howard isomorphism --- proposition as types

lambda calculas

statement can be true of false

proposition correspond to types in programming

true or false / inhabitted or uninhabitted (type has value or not inside)


| implication a=>b | a ∨ b      | a ∧ b  | false       | true          |
| function         | Either a b | (a,b)  | void        | ()            |
| b^a(exponential) | a × b      | a or b | initial obj | terminal objt |


((a=>b), a) -> b

a=>b ∧ a -> b

one-to-one relation between logic an type

mathematic people build a theory in logic; then CS people will take it and think how can I implement this in language, like the linear type or structural type system.

[substructural type system](https://www.wikiwand.com/en/Substructural_type_system)



