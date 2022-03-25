#include "holberton.h"
#include <math.h>
/**
 * modulus - return the modulus
 * @c: complex number
 * Return: c
 */
double modulus(complex c)
{
	double modulus;

	modulus = sqrt(pow(c.re, 2) + pow(c.im, 2));
	return (modulus);
}
