# Cat 5.1 Coproducts, sum types
[previous lecture review]:
* product, univeral construction for product.
* today's lecture is dual work of previous lecture --- coprodcut.
* Opposite Category, **reversing the arrow**, get coproduct
* similarly, monad-comonad, monoid-comonoid.

[lecture]
	• fix 2 object, find what it will produce.
	• 2 injections
	• like product, a very Category way: find all other objects.
	• then unique morphsim.

also have 2 commute triangle, differently from production, which is from fake ones to true one, this time is from the true one to fake ones

![many product candidates and the right one](https://s14.postimg.org/m4wfvoqm9/screenshot_12.png)

## projection vs. injection

![projection and injection](https://s14.postimg.org/tgxamzjb5/screenshot_6.png)

because in right diagram, the <a,b,c,i,j> is the universal construction, he is the best, the best fit for this pattern. we want this injection, will inject the whole set, witout shrinking, without collapse anything. 

we just take the whole set 'a' into the set 'c', and we do the same way with 'b'. It's the ideal match, no more, no less, just kick the edge. 

![no more, no less](https://s14.postimg.org/qpe0wq0bl/screenshot_7.png)

## tagged union in Coproduct
### tagged union and ordinay union
what if the 'a' and 'b' are same set? what if 'a' and 'b' have intersection?
	1. the union of a set with itself, is this set itself
	2. I can tag the repeated elements, and say that, although they are same elemetns, but with different tags, this is from 'a', another is from 'b'. this is called discriminated union: https://www.wikiwand.com/en/Tagged_union
	
![disjoin union vs. union](https://s14.postimg.org/56stvxk35/screenshot_8.png)

we can make c as a disjoint union, and c' as a ordinary union, but we can not reverse this, you CANNOT make c as a union and c' as a disjoint union.

**why**?

ONE element in c will map to TWO elements in c', this is NOT allowed as a function.
![Not a Function](https://s14.postimg.org/5yvhuvo7l/screenshot_9.png)

this is point view of Set Theory, when your union 2 sets who have duplicated elements, and these elements will keep in union result with different tags.

## product-type and sum-type

| product-type                              | sum-type                                                                        |
|-------------------------------------------|---------------------------------------------------------------------------------|
| Tuple(and other collection type) in scala | tagged union can only have one of the types, and with a tag                     |
| can contain many types, like (Int,Bool)   | to specify which type of the current value stored in the tagged union datatype. |

### sum-type
``` hasekll:
data Either a b = Left a | Right b
```

``` scala:
val x: Either[Int, String] = Right("good")
```

These constructor directly correspond to injections, like all "**may or**" types in scala: 
	* Either: may this or that
	* Option: may value or None
	* Try: may value or Exception
    * Future: may value(avaiable at sometime) or Exception

![may or types Coproductin sum-type](https://s14.postimg.org/rp8x5urwx/screenshot_10.png)




### product-type

many collection type in scala is product-type:
* Tuple: `(Int, Boolean)`
* Array: `Array(Boolean, Boolean)`
* List, Seq etc.

![pattern match and production](https://s14.postimg.org/mdu0lcvm9/screenshot_11.png)

## summarization
So, now I know that, match pattern in scala comes from Categorical Production ; and "may or" types( and you can define your own "may or" type by algebraic datatype which is pratical use of  tagged union)in scala comes from the opposite thing Categorical Coprodcution. And I also know that, why "may or" types all can do pattern matching --- using match case clause.

Category: product type, sum type, unit, void
product-type, sum-type, unity, void are fundation of the type system. Many people said that: 

> In Haskell type system, half is product-type, half is sum-type, and if there is a third half, it must be the combination of them.


# Cat 5.2 Algebraic data types

## for product-type

### production similar with monoid in 3 similar ways ###

we have a multiplication ,the product is similar to multiplicaiton, what does it mean that such a multiplication?
It means we have a **monoid**, at least. **Monoid** is something **associative**, something **multiplication**, something **unit**. But, what we want to talk about is **types**, **algebraic data types**. Is product in the algebraic datatype has same way as **monoid**. 


> **remeber monoid?**
> 1. **Integer** form a monoid under **production**, with **unity** 1;
> 2. **Integer** form a monoid under **addition**, with **unity** 0;
> 3. **String** form a monoid under **concatenation**, with **unity** empty string
> 4. **List** form a monoid, under **append**, with **unity** empty list.
> tips ： this is why in Haskell string is list, because they are both monoid.

you can see that, all the operator who makes a set a monoid is something like a **multiplication**, a **combination**, not a union.

so we can say a monoid have 3 attributes:
1. **unit** in set
2. **associative** on operator
3. **combination** on view


#### symmetric up to isomorphism vs. symmetric(not related to monoid, just show trait of isomorphism) ####

product produce some pairs: (a,b) = (b,a) . This 2 pairs are not same, but they have same information, the only difference is just the way of encoding --- Not Same, but isomorphic. We can define a function like "swap", which is a isomorphism between (a,b) and (b,a), in other words: They are not same, but same up to isomorphism.

![swap is a isomorphism between (a,b) and (b,a)](https://s14.postimg.org/c9w3xz7wh/screenshot_4.png)

``` haskell
// (a,b)!=(b,a)
swap:: (a,b)->(b,a)
swap p = (snd p, fst p)
swap_reverse q = (snd q, fst q)
```

it's obvious that swap is a isomorphism between (a,b) and (b,a), so we can say (a,b) and (b,a) is *isomorphic*

#### associative up to isomorphism vs. associative ####

If the production as an binary operator which under which build up a monoid, must statisfy associative rule: ((a,b),c) = (a,(b,c)). no, it's not satisfied. But they have the same information, but rearrange them, similarly we can find a function like "assoc", which is isomorphism between ((a,b),c) and (a,(b,c)), in other words:  The production is not associative, but associative up to isomorphism.

``` haskell
// ((a,b),c) != (a,(b,c))
assoc :: ((a,b),c) -> (a,(b,c))
assoc p = <some pattern match clause>
assoc_reverse q = <some pattern match clause>
```

vs. monid-associative for Integer under multiplication: 3*(4*5) = (3*4)*5

* production: an **similar**-associativity on **type**(**set**)
* monoid: an **true**-associativity on **element**

#### Unit up to isomorphism vs. Unit ####

the same thing can apply to the unit: production dose not satisfy `(a,()) = a`, but they have the same information. we also can find a function like "munit", which is a isomorphism between (a,()) and a.

``` haskell
// (a,()) != a
munit :: (a,()) -> a
munit p = fst p
munit_reverse q = (q,())
```

vs. monid-unit for Integer under multiplication: 3*1 = 3

* production: an **similar**-unit on **type**(**set**)
* monoid: an **true**-unit on **element**

### production different with monoid in the way of many sets to one set ###

> **remeber monoid?**
> 1. Integer form a monoid under production, with unity 1;
> 2. Integer form a monoid under addition, with unity 0;
> 3. String form a monoid under concatenation, with unity empty string
> 4. List form a monoid, under append, with unity empty list.
> tips ： this is why in Haskell string is list, because they are both monoid.

So you can find that, monoid is just **a special set** (for unit), with some **special operator on set**(for binary operator).

what about the product?

It's something related to many types( or we can say many sets)

| product                        | monoid                      |
|--------------------------------|-----------------------------|
| type of type operate on type   | a set and operat on element |
| similar assoc(if isomor exist) | true assoc                  |
| similar unit(if isomor exist)  | true unit                   |


## for sum-type
1. symmetric up to isomorphism

``` haskell
// Either a b ~ Either b a
// easy to find a functin to do that
```

2. associative up to isomorphism

``` haskell
data Triple a b c = Left a
                  | Right c 
                  | Middle b        
// also easy to define a type to do that                  
```

3. unit up to isomorphism

``` haskell
Either a void ~ a
```


## **why not 'void' in product-type?** or **why not 'unit' in sum-type?** 
``` scala
def f(e: Either[Int,Unit]): Int = {
  e match {
    case Left(x) => x
    case Right(x) => 0
  }
}
```

``` scala
// g: a => Either(a,b)
// you only can get a "left" value
def g(a: Int): Either[Int,Unit] = {Left(a)}
// or a "right" value
def g(a: Int): Either[Int,Unit] = {Right(println("0"))}
// you can not get both at same time
```

you can see that, because the `Either` is a **sum-type**, a "may or" type,it's essentially a tagged union. you can never get all the value at one time. So for **f** you can not get a **g** to make a **idendity** function by composing them.

From another point of view, `object a <---> object Either a or unit`
    * `a`(see as a set) has **num(a)** elements;
    * `Either a or unit` has **num(a) + 1** elements;


the similar situtation for void of product-type.
    * `a`(see as a set) has **num(a)** elements;
    * `Tuple(a, void)` has **0** elements;

**the number of values they can represet is not equall, they MUST NOT isomorphic.**

So,**unit in product-type** and **void in sum-type**, which is just similar to algebraic computation: 
    * n*1=n; 
    * n+0=n;

## why named Algebraic datatype?

By what showed in last 2 sections above, we can generalize the isomorphisms to a symbol *, whick some like the muplitply:

* a * 1 = a ; a munit () = a
* (a * b) * c = a * (b * c) ; (a,b) assoc c = a assoc (b,c)

this is why we called it that.


## we now have two monoid-like things, how to combine them.
we can now infer some formulas(which also should append with "**up to isomorphism**", and just use symbol **~** which means **isomorphic**)

| algebric computation | algebraic data types                |
|----------------------|-------------------------------------|
| a * 0 = 0            | (a,void) ~ void                     |
| a*(b+c) = a*b+a*c    | (a,Either b c) ~ Either (a,b) (a,c) |
| 2 = 1 + 1            | Boolean ~ Either True False         |
| a + 0                | Option a or None                    |


### Ring
What is this structure called, both multiplication and addition in the same thing --- **ring**

A really Ring has some other things, like inversement of addition, inversement of multiplication.

If a Ring don't have all these inverse elements, it's called **semiring** or **rig**(no spell mistake) = **Ring without negative**.


### algebraic equation

sleight of hand

#### haskell to algebraic equation
`data List a = Nil | cons a (List a)`
It is so **self-explanatory** , and give a **recursive** definition of `List` 
> - "what is a List"
> - "it's empty or concate a value with a List"

![algebraic datatype for recursion equation](https://s14.postimg.org/5lh4s27m9/screenshot_14.png)


`data List a = Nil | cons a (List a)`

In algebraic datatypes, we can find the algebraic equation:

```
l(a) = 1 + a * l(a)
     = 1 + a * (1 + a * l(a))
     = ...
     = 1 + a + a*a + a*a*a + ...
```

#### algebraic equation to haskell
then, what is this `1+a+a^2+a^3+...`, this is just what we say in haskell

``` haskell
List(Nothing) | List a | List a a | List a a a | List a ... | List a_infinite 
```

which means **all kinds of List**(has 0~infinite elements) who has the type of element `a`

``` haskell
data List a = Nil | Cons a (List a)
```
