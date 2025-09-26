import logging
import math

logging.basicConfig(filename='app.log', level=logging.DEBUG)

def findingTangent(sin_alpha, cos_alpha):
    logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    try:
        if not isinstance(sin_alpha, (int, float)) or not isinstance(cos_alpha, (int, float)):
            logging.critical("The tangent of the angle alpha is not defined.")
        elif cos_alpha == 0:
            logging.warning("The cosine of the angle alpha = 0. The tangent is not defined.")
        else:
            tan_alpha = sin_alpha / cos_alpha
            logging.debug(f"The value of the tangent of the angle alpha is found = {tan_alpha}")
    except:
        logging.critical("The tangent of the angle alpha is not defined.")


findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)