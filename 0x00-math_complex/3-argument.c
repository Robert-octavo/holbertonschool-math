#include "holberton.h"
#include <math.h>
/**
 * argument - return the argument
 * @c: complex number
 * Return: duoble
 */
double argument(complex c)
{
	double argument;
	argument = atan(c.im / c.re);
	return (argument);
}
