module Lib
    ( someFunc
    ) where

{-someFunc :: IO ()
someFunc = putStrLn "someFunc"-}

someFunc :: IO ()
someFunc = print action

sumar::[Int]->Int
sumar [ ] = 0
sumar (x:xs) = x + sumar(xs)

--action = sumar [5,4,7,8]

invertir::Ord a=>[a]->[a]
invertir [ ] = [ ]
invertir (x:xs) = (invertir xs)++[x]

--action = invertir [5,4,7,8]

igualLista:: Eq a => [a]->[a]->Bool
igualLista l1 l2 = l1 == l2

 --action = igualLista ["Hola","Mundo"] ["Mundo","Hola"]

lista_ordenada::Ord a=>[a]->Bool
lista_ordenada [] = True
lista_ordenada [_] = True
lista_ordenada (x:y:xs) = (x<=y) && lista_ordenada (y:xs)

--action = lista_ordenada ['a','b','c','d']

mostrar_ubicacion::Ord a=>[a]->Int->a
mostrar_ubicacion l n = l!!n

--action = mostrar_ubicacion [15,25,26,28] 2

mayor::[Int]->Int
mayor [x] = x
mayor (x:xs)
    | x > mayor(xs) = x
    | otherwise = mayor(xs)

--action = mayor [78,24,56,93,21,237,46,74,125]

contarpares::[Int]->Int
contarpares []=0
contarpares lista= length [x | x <- lista, mod x 2 ==0]

--action = contarpares [5,4,7,8]

cuadrados::[Int]->[Int]
cuadrados [ ] = [ ]
cuadrados l = [x*x| x <- l]

--action = cuadrados [1..10]

divisible::Int->Int->Bool
divisible x y = (mod x y) ==0

divisibles::Int->[Int]
divisibles x = [y | y <-[1..x],divisible x y]

esPrimo::Int->Bool
esPrimo n = length (divisibles n) <=2

primos::Int->[Int]
primos n = [x | x <-[1..n],esPrimo x]

action = primos 100
