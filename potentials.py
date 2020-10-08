from math import pi
from point import Point, distance


def __pre_potential__(receiver_p: Point, source_a: Point, source_b: Point) -> float:
    """Вычилисть значение, используемое в вычислении потенциала.

    :param receiver_p: координата точки приёмника
    :param source_a: координата A электрода источника поля
    :param source_b: координата B электрода источника поля

    :return: значение
    """
    return 1 / distance(receiver_p, source_b) - 1 / distance(receiver_p, source_a)


def compute_electric_field_potential_difference(
        receiver_p: Point, source_a: Point, source_b: Point,
        sigma: float, amperage: float) -> float:
    """Вычислить разность потенциалов в точке P.

    :param receiver_p: точка P приёмника тока
    :param source_a: координата A электрода источника поля
    :param source_b: координата B электрода источника поля
    :param sigma: удельная электрическая проводимость
    :param amperage: сила тока

    :return: значение потенциала.
    """

    coeff = amperage / (2 * pi * sigma)
    return coeff * (1 / distance(receiver_p, source_b) - 1 / distance(receiver_p, source_a))


def compute_electric_field_potential_difference(
        receiver_m: Point, receiver_n: Point, source_a: Point, source_b: Point,
        sigma: float, amperage: float) -> float:
    """Вычислить разность потенциалов в линии MN.

    :param receiver_m: точка M приёмника тока
    :param receiver_n: точка N приёмника тока
    :param source_a: координата A электрода источника поля
    :param source_b: координата B электрода источника поля
    :param sigma: удельная электрическая проводимость
    :param amperage: сила тока

    :return: значение потенциала.
    """

    coeff = amperage / (2 * pi * sigma)
    m_point_potential = __pre_potential__(receiver_m, source_a, source_b)
    n_point_potential = __pre_potential__(receiver_n, source_a, source_b)
    return coeff * (m_point_potential - n_point_potential)


def compute_potential_derivative(
        receiver_m: Point, receiver_n: Point, source_a: Point, source_b: Point,
        sigma_i: float, amperage: float) -> float:
    """Вычислить значение производной потенциала по сигма в точке sigma_i.


    :param receiver_m: точка M приёмника тока
    :param receiver_n: точка N приёмника тока
    :param source_a: координата A электрода источника поля
    :param source_b: координата B электрода источника поля
    :param sigma_i: i-я удельная электрическая проводимость
    :param amperage: сила тока

    :return: значение производной в точке sigma_i.
    """

    sigma_square = sigma_i ** 2
    derivative_coeff = - amperage / (2 * pi * sigma_square)

    m_point_potential = __pre_potential__(receiver_m, source_a, source_b)
    n_point_potential = __pre_potential__(receiver_n, source_a, source_b)
    return derivative_coeff * (m_point_potential - n_point_potential)