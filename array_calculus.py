#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Abby Wheaton and Frank Entriken
# Student ID: 2299246, 2298368
# Email: wheaton@chapman.edu, entriken@chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW09
###



import numpy as np
import matplotlib.pyplot as plt


def gradient(a, b, n):
    dx = (b-a)/(n-1)
    x = np.linspace(a, b, n)
    Df = np.zeros((n, n))
    one_array = np.ones(len(Df)-1)
    np.fill_diagonal(Df[1:], -one_array)
    np.fill_diagonal(Df[:, 1:], one_array)
    Df[0][0] = -2
    Df[0][1] = 2
    Df[n-1][n-1] = 2
    Df[n-1][n-2] = -2
    Df = (1/(2*dx))*Df
    return Df

def f_plot(a, b, n):
    x = np.linspace(a, b, n)
    fx = [i**2 for i in x]
    Df = gradient(a, b, n)
    f_grad = Df@fx
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of $x^2$ and its derivative")
    
def f_plot_grad(a, b, n):
    x = np.linspace(a, b, n)
    fx = [i**2 for i in x]
    f_grad = np.gradient(fx)
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of $x^2$ and its derivative using np.gradient")
    
def f_second(a, b, n):
    x = np.linspace(a, b, n)
    fx = [i**2 for i in x]
    D = gradient(a, b, n)
    Df = D@D
    f_grad = D@fx
    f_2_grad = Df@fx
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.plot(x, f_2_grad, label = "f''(x)")
    plt.legend()
    plt.title("Graph of $x^2$ and its first and second derivatives")
    
def s_plot(a, b, n):
    x = np.linspace(a, b, n)
    fx = [np.sin(i) for i in x]
    Df = gradient(a, b, n)
    f_grad = Df@fx
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of sin(x) and its derivative")
    
def s_plot_grad(a, b, n):
    x = np.linspace(a, b, n)
    fx = [np.sin(i) for i in x]
    f_grad = np.gradient(fx)
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of sin(x) and its derivative using np.gradient")
    
def g_plot(a, b, n):
    x = np.linspace(a, b, n)
    fx = [(np.divide((np.exp(np.divide(-(i**2), 2))), np.sqrt(2*np.pi))) for i in x]
    Df = gradient(a, b, n)
    f_grad = Df@fx
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of $e^{-x^2/2}/\sqrt{2\pi}$ and its derivative")
    
def g_plot_grad(a, b, n):
    x = np.linspace(a, b, n)
    fx = [(np.divide((np.exp(np.divide(-(i**2), 2))), np.sqrt(2*np.pi))) for i in x]
    f_grad = np.gradient(fx)
    plt.plot(x, fx, label = "f(x)")
    plt.plot(x, f_grad, label = "f'(x)")
    plt.legend()
    plt.title("Graph of $e^{-x^2/2}/\sqrt{2\pi}$ and its derivative using np.gradient")