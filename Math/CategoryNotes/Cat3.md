# Cat 3.1 Examples of categories, orders, monoids

Review previous: reformulation of the language of the arrows or morphisms or function between sets. 

from previous course, we know about something of Cat of sets who as a model of Cat of type and function.

Now, Let's exapnd our horizons and look at other interesting Cat.

**what is the simplest category?**
Cat who has 0 object. if no object, then no arrows, because arrow is starting from one object to another.
0 object, 0 arrow is Cat?
Rember the 3 axioms of Cat?

1. every object has a circle arrow
2. left/right identity function
3. associativety: (f*g)*h = f*(g*h)

> yes, it satisfy all 3 axiom (maybe it strange to think about)

## 0
This Cat is empty, call it 0, not to be confused with number 0.

but this category is useless, unless used in a **context** 
```
0 is useless
but combine with 1, it's usefull
10
1000
1000000
```

**what is the context for this category**
context would have been important if we had a **category of all categories**.

there is a category of small categories in which objects form a set, and not some big things.

there is also category of all categories, but it is much more insidious, because you have to work
with pieces that are not sets.


## 1
this is 1 object Cat, it's pretty useless category by itself, Except again, **in the context of the category of all categories**. 

then she will give you some information without explanation until a terminal object in the category of categories.

### Catgetory from Graph
they are looks similar when draw, but very different:
1. Cat will **automatically** adding arrows because of **composition -- axiom2**
![auto adding arrows](https://i.imgur.com/QvrJ9wY.jpg)
    - when exist: f :: a->b, g :: b->c, then there must be an arrow from a->c.
    - when Cat having more objects, this process will go on and on.

2. For a Cat, although number of arrows are growing on and on, but some arrows are totally same because of **association -- axiom2**, this will slow down the growing number of arrows.

so, in Cat, it's very normal to adding things **freely** and automatically by the 3 axioms.

it is a structure called free construct(or **svobodnuyu** category)

Such a category called: [[free]] category

### extend **free** to other structure
> **free** monoid
In general, if you have any other structure, not a category or a graph, you can apply the same process to create a free piece, like a **free group**, **free monoid** and so on

this is a typical construction for the theory of categories.

## Other kind of categories: orders
Orders are categories in which the arrows are not functions.
But in the category of right-hand is something else, is **not a function**, not some abstract thing, but **attitude** or a **relation**.

In particular, it is interesting relation "less than or equal to"

![arrow is LT](https://i.imgur.com/ustiHD7.jpg)

we can say: **a comes before b in some order**

There are 3 kinds of order:
1. pre-order
2. partial order
3. **total order**

we are more familiar with total order, because they are used when sorting on elements, it must be defined **total order**

### pre-order is composable
But, the simplest order we can have is the **pre-order**. Pre-order here is imposed the minimum conditions(restriction). The minimum restriction is it must be **composable**:

> if a<=b, b<=c, then a<=c.

![preorder is composable](https://i.imgur.com/s0bJvVm.jpg)

also 
> if a<=b, we can also has b<=a

![a->b->a loop](https://i.imgur.com/gA1GcNk.jpg)

the preorder will automatically composable

### pre-order is associativity
Why associative?
Because the two objects in this scenario are connected or not:
1. 1 arrow between a and b
2. 0 arrow between a and b
3. >1 arrows is not possible

> (<= <=)<= equal to <=(<= <=)

> If a and b are in a relation, then there is an arrow from a to b, if else no arrow between a and b.

> Here the situation is **not possible with many arrows** between objects.


function vs. relation(attitude)
* function is **infinite** choices
* relation is **binary** choices

Total order vs. pre-order vs. partial order
* total order: between **any 2 objects** there is an **arrow**.
* pre-order: may have arrow or not
* partial order: may have arrow or not

### pre-order is Identity.
> a <= a

### Thin Category
Such a category like pre-order, called: [[thin]] category.
Only <= 1 arrow between two objects, it's looks so Thin.

Any thin category corresponds to preorder,every preorder corresponds to a thin category, they are 1 to 1 corresponding.

So like 1 to Natural Number, to all kinds of orders the preorder is the simplest. 

because it is just a category, although it's a thin category.

#### Hom-Set

hom-set hom(x,y) is the collection of all **morphisms** from x to y. 

every arrow has its name what we called home-set:
> hom-set : C(a,b) // all morphism from a to b
> or
> hom-set : C(a,a) // all morphism from a to a 

It's a set of arrows, in the set theory it's a set. The thin category is small category of any Hom-set is either a singleton or empty. 

We will talk about Hom-set in future.

We can impose more restriction to get another category like **partial order**, we don't like loop in pre-order. partial Order has no loops:
> if a->b, absolutely not b->a

### Pratial-order
* partial-order has more restriction than pre-order;
* partial-order is like DAG(direted no-loop graph)

partial order vs. total order
* total order has arrow between any two object;
* partial order don't have all pair connected.

### Invertible and Epimorphism and Monomorphism in Thin Category

In thin category, something epimorphism and monomorphism doesn't have to be invertible.

Function in Set theory,is both injective and surjective, is invertible, and isomorphism, it's also called bijection.

Rember that:
1. fg = fg' => g = g' : monomorphism
2. gf = g'f => g = g' : epimorphism

![epi and mono](https://i.imgur.com/k8l5Bt7.jpg)

they all have multiple arrows between two object. 

But this is **not allowed** in Thin Category.

> So, every arrow in the pre-order is monomorphism and epimorphism.

So, in Thin Cagegory , an arrow is epi and mono, dose not have to be invertible.

when refer to Partial order, invertible is absolutely dosen't exist, because it dese not allow **loop**, it's a DAG.

### Thick Category
Thin Category defines a relation, only allow 1 or 0 arrow between 2 objects.
Thick Categroy also defines a relation, but with allowing many arrows between 2 objects, each arrow can be seen as a prove th the relation.

This is a different approach, another intuition, and the proof relevant things are becoming more important, in the **homotopy** theory of types [HoTT].

HoTT build on the assumption that it is insufficient to show the relationship of one to the other, there are different ways of such evidence, and they are not equivalent.




## Talk back to singleton category: monoid

![monoid](https://i.imgur.com/ZMMooRV.jpg)

Singleton Categoy, can of course have many circle arrow, and consider the axiom2 --- **composition**, when one arrow's output is another arrow's input, they can compose together.

The intresting thing is that, **all the Singleton Category's arrow are composable**, because there is only 1 object, every arrow begin and end in this object.

This thing has a name --- **monoid**

**monoid** means single.

Any category has a single object, it's a **monoid**

### Intuition: how to define monoid in Set theory and algebra
> set, operator -- muliplication -- binary operator 
> --- impose condition on set --- unit is ele,like 1

Monoid is a special set, with a operator to demonstrait its trait.
we impose **1 restriction** respectively on the **binary operater** and **set**, to build a monoid:

**Restriction on set: Unity**

    - we want **one elment** in the Set to be **unity**.
    - operator(unity, other) = oter; operator(other, unity)= other

**Restriction on operator: Associativity**

    - we want **an binary operator** which obey the **associativity**
    - (a oper b) oper c = a oper (b oper c)
    
> R1 + R2 ==> for any a: e * a = a * e = e

![Unit and Associativity for monoid](https://i.imgur.com/3v9FpzF.jpg)

> If there is something both **unity and associativity**, it's Monoid.

> monoid in Set Theory and algebra = unity + associativity

you see that, we now talk about the **details**, the **element level**, it's the definition of monoid in Set Thoery. Keep in mind that we have not talked about Categtory definiton of monoid.

### Examples of Monoid in Set Theroy:

For a monid, you need follow the formular to describe its structure

> ... form ... under ... with
> <kindofSet> **form** a monoid **under** <opertor>, **with** unity <element>

1. Integer form a monoid under production, with unity 1;
2. Integer form a monoid under addition, with unity 0;
3. String form a monoid under concatenation, with unity empty string
4. List form a monoid, under append, with unity empty list.
tips ： this is why in Haskell string is list, because they are both a monoid.

### Monoid in Category Theory
Remember that, 

| Set theory                                        | Category theory                               |
|---------------------------------------------------|-----------------------------------------------|
| detail                                            | whole,no detail                               |
| many different defintion use many different terms | use and ONLY use function describe everything |

**now Monoid in Category is also follow the habit of Category theory: use and ONLY use function to define a Monoid.**

![monoid in Category Theory and Set Theory](https://i.imgur.com/ViNfr7h.jpg)

**How to do that**
In a **1 object Category**, we ignore all details only left the object and morphism(and morphism set: Hom-set). So we have:
1. 1 object
2. hom-set: 1 morphism---Identity

now we talk about **one special kind of 1 object Category**, with not only Identity morphism, but many morphism from this object to this object, we have:
1. 1 object
2. Hom-set: many morphism from and to this object

**then, we will find hom-set of this Category is a Monoid in Set theory:**
1. we have a unity in this set:
    - Identity morphism;
2. we have a operator that can do association:
    - Category has 3 axioms: Identity, Composable, Associativity
    - although we don't know what is exactly the operator is ,but we know this operator is a morphism/arrow in Category, then it must obey the 3 axioms, so it must be associativity

then we can say, Hom-set of this special Category is a Monoid.

So again, we made it, we win!
we use and ONLY use function to define a monoid in Category: if hom-set of an Category is a Monoid in Set theory, then this Category is a monoid.

### Monoid vs. strongly typed system in programming language
General category(specially category of set), correspond to strongly typed, which is kind of type system, you CAN NOT actually compose any 2 function, every function's input and output type can't match each other --- type is devided every precisely, too details.

Oppose to that, Monoid is a kind of weak type system, or even no types, every 2 functions can compose.

### more about the totoal order, partial order and pre-order about inclusion relation
summary: more details about the total order, partial oder, pre-order.

Let's define a relation on sets, a **inclusion relation**, what set is to be a subset of another.

Is this inclusion relation a total order, partial order, or pre-order?

**what would we check？**
1. identity
    - a ⊆ a
2. composition
    - a ⊆ b, b ⊆ c, then a ⊆ c
3. associativity
    - (a ⊆ b) ⊆ c = a ⊆ (b ⊆ c)


**Identity morphism is a kind of reflexivity**

> tips: the term "reflexivity" will more and more often occur in our followed lectures.

just review the 3 order:
| total order           | partial order | pre-order                          |
|-----------------------|---------------|------------------------------------|
| fully connected graph | DAG           | Thin Category: 0/1 connected graph |


> tips: 
> 偏序只对**部分元素**存在关系R，全序对集合中**任意两个元素**都有关系R。
> 例如：
> 集合的包含关系就是半序，也就是偏序，因为**两个集合可以互不包含**；
> 实数中的大小关系是全序，两个实数必有一个大于等于另一个；

> 我理解：
> 全序（total order） 就是所有元素pair都可以放在一条线上，实际上 total order 也叫 line order, 这条线的前后关系就是关系 R 的运算顺序。
> 也就是集合的所有点都存在关系 R。
> 偏序（partial order）就是不是所有的元素pair都存在关系 R，也就是说他存在不止一条线。



# Cat 3.2 Kleisli Category

think about this real programming task:
> Refact our porject to: every time invocation of a function, log its name,augument and action.
> This means that every function invocation must leave a trail.

``` Haskell
bool negate(bool x) {
  return !x
}
```
will change to:
``` Haskell
// add a global log to store every function trail.
string log = ""

bool negate(bool x) {
  // add some operation to log action of funciton
  log += "not!"
  return !x
}
```

this is the simplest way to handle this requirement,
but,~simplicity is not easy~

For this solution, we create **dependence**, the hidden **relationship** between function and log variable.
Something like the long-range interations in quantum mechanics --- **a long distance dependency**. The risk is once you remove
the log variable, your whole program will fail down. The complexity will exponentially grow when we add multi-threading.

Now lets move a little bit, to make this function a **more purer** function, means that no side-effect, all the states changed will explicitly show in the return expression:

change codes again:
``` Haskell
string log = ""
// make log as an augument of function, which you must explicitly passed a value.
pair<bool,string> negate(bool x, string log) {
  // compose the "log" and "negate", refect this 2 action in result returned.
  return make_pair(!x, log+"not!")
}
```

now, we don't worry about the vanishment of log variable,because everytime you call a function you must explicityly specify the place where you log it .

But our function is just **more purer**, not **absolutely pure**.

remember that:
> when you funtion is pure, you can memoise it(or tabulate it)

This means that everytime you input the same value, function must return the same result.

``` Haskell
// assume log file now is empty.
negate(true, log) -> (fail, "" + "not!")
negate(true, log) -> (fail, "not!" + "not!")
```
you see that, same input lead to different output.

So, this a good solutin, but no quite!

the key issue is caused by "+", so again change:


``` Haskell
string log = ""
pair<bool,string> negate(bool x) {
  return make_pair(!x, "not!")
}
```
But, who concatenate the string with orgininal content of log?
we should do some function composition to handle this, but by now everthing is OK, right? We have a pure function, his functionality is explicitly and unity.

The next step is to concern about how to do composition: what if we change the method of composition, modify the way we compose function.

Let's define a new way of composing fucntions.

the default composition:
``` scala
def compose[A,B,C](fn1: A=>B, fn2: B=>C):A=>C = (a:A) => fn2(fn1(a)))

```

now we change the way of composing, which correspond to the function **negate** we defined above.
``` scala
def compose[A,B,C](fn1: A=>(B,String), fn2: B=>(C,String):A=>(C,String) = {
  (a:A) => {
    val p1 = fn1(a)
    val p2 = fn2(p1._1)
    (p2._1, p1._2 + p2._2)
  }
}

```
Every time you do some composition of 2 functions, you must tip yourself that, dose this compose make some hint about a Category?

### Composable?
Of course it is

### Associativity?
It's obviously that the default composition is associative, but when we add a String to make type of result a Tuple, is that will change the associativity? 
No, add a string to return type ,will not change associativity. because we just do that by **string concatenation**:
```
string a,b,c
(a+b)+c isEqual a+(b+c)
```
String concatenation is Associative, and more than that, it's a Monoid

### Identity?
String forms a Monoid under concatenation with Identity empty string.
So this new compose function has Identity.

### Build new Category from exist Category by adding Monoid
```
// "+" here means some way of combining, eg Tuple
Category + Monoid = Category
default compose + String under concatenation with empty string = Catetory
default compose + Integer under addition with 0 = Catetory
default compose + List under append with empty list = Catetory
```
So now, not only the String can be log, but any monoid can be log, because log is just additive to make One Cat to another Cat.

now let's go back to the original problem, and with a bird eye view:
1. we have a bunch of functions, they may forms a Cat with a type system.
2. then we want to add some operation to every funtions.
3. The only restriction to the operation is it must be an Monoid.


### Kleisli Category
> keep in mind that :
> Kleisli Cat has the **same objects** with the original Cat from wich we build the Kleisli Cat, but **different arrows**

I build a category whose object is A,B,C --- types.
But arrows in this Category is not the function as you see as before.
* usual function(arrows): A ---> B
* funtion in this scenario: A ---> (B,String)

(B, String) is called **embellishment**.

for this `A ---> (B,String)` , I know:
1. what is Identity
2. I know how to do composition
3. I know how to do assocaitivity

so I get a Category, this kind of Category actually has its name: **Kleisli Category**.

`A ---> (B,String)`, called Kleisli Arrow, these embellished funtions.

In scala, this something like:
``` scala
// Int ---> Option[String]
def arr(a: Int): Option[String] = Some(a.toString)
```

> Kleisli Arraow can de defined a huge kinds of **embellishments**, what show above is just one example of **embellishment** using **pairing** the result with string. There are many other **embellishment**, and very usefull.

### Monad

These arrows are composable is actually because these **embellishment** is the Monad.

We haven't talk about **monad**, but **monad** is nothing special, it's just the **way of composing** special types of functions.

people can't understant what is **monad**, is because of the imperative language background.

In imperative programming, we think so --- keyword "return" :
1. call funtion **return** something
2. then we do something with the **returned** result.

In functioanl programming, we think so --- keyword "compose" : 
1. I **compose** a bunch of operations using function composition.
2. what if I use a **different composition**, also function composition, but with some kind of flare, something additional(like combine with Monoid), I have **one degree of freeedom** when defining a new composition. If I use this **degree of freedom**, I'm using a **Monad**.

> Monad key word: 
> way of composing; 
> one degree of freedom
