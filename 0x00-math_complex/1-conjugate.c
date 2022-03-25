#include "holberton.h"
#include <math.h>
/**
 * conjugate - return the conjugate
 * @c: complex number
 * Return: c
 */
complex conjugate(complex c)
{
	c.im *= -1;
	return (c);
}
