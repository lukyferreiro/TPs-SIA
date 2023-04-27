import numpy as np
import math

class Perceptron:
    
    def __init__(self, input_data, expected_data, perceptron_type, learning_rate, epochs, beta, min_error, training_percentage, k):
        self.weights = np.zeros(len(input_data[0]))
        self.training_percentage = training_percentage

        self.input_data = input_data
        self.expected_data = expected_data

        self.perceptron_type = perceptron_type
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.beta = beta
        self.min_error = min_error
        self.train_MSE = -1
        self.k_fold = k
        self.min, self.max = self.__calculate_min_and_max(expected_data)

    # Inicializar conjuntos de training y testing
    def __divide_data_by_percentage(self, input, expected, p):
        num_rows = int(p * input.shape[0])

        idx = np.random.permutation(input.shape[0])

        t1 = input[idx[:num_rows], :]
        e1 = expected[idx[:num_rows]]

        t2 = input[idx[num_rows:], :]
        e2 = expected[idx[num_rows:]]

        return t1, e1, t2, e2

    # Función de entrenamiento por porcentajes
    def train(self):
        if self.k_fold != -1:
            raise("No puede entrenarse con porcentaje si se eligio k_fold")

        current_epoch = 0
        finished = False
        
        train_input, train_expected_data, test_input, test_expected_data = self.__divide_data_by_percentage(self.input_data, self.expected_data, self.training_percentage)
        
        train_len = len(train_input)
        Os = np.empty(train_len)
        mse_errors = np.empty(self.epochs)

        while current_epoch < self.epochs and not finished:
            for j in range(train_len):
                x = np.array(train_input[j])
                h = np.dot(self.weights, x)
                Os[j] = self.activation(h)
                expected = train_expected_data[j]
                self.weights += self.calculate_delta_w(x, expected, Os[j])

            mse_errors[current_epoch] = self.__mid_square_error(Os, train_expected_data)

            # TODO check porque nunca entra aca, mse tiene vlaores altos
            if (mse_errors[current_epoch] < self.min_error):
                finished = True

            current_epoch += 1
        
        # Guardo el MSE error al finalizar el entrenamiento
        self.train_MSE = mse_errors[current_epoch - 1]

        print("Finished Training")

        self.test(test_input, test_expected_data)

        return self.weights, mse_errors
    
    def train_k_fold(self):
        if self.k_fold == -1:
            raise("No puede entrenarse con k_fold si se eligio porcentaje")
        
        original_weights = self.weights

        input_data_sets = np.array_split(self.input_data, self.k_fold)
        expected_data_sets = np.array_split(self.expected_data, self.k_fold)

        print(input_data_sets)

        MSEs_array_train = np.empty(self.k_fold)
        MSEs_array_test = np.empty(self.k_fold)

        all_weights = np.array([])

        for k in range(self.k_fold):
            self.weights = original_weights

            # TODO. arreglar 
            current_train = np.delete(self.input_data, input_data_sets[k], axis=0)
            current_expected = np.delete(self.expected_data, expected_data_sets[k])
            train_len = len(current_train)

            Os = np.empty(train_len)
            mse_errors = np.empty(self.epochs)

            while current_epoch < self.epochs and not finished:
                for j in range(train_len):
                    x = np.array(current_train[j])
                    h = np.dot(self.weights, x)
                    Os[j] = self.activation(h)
                    expected = current_expected[j]
                    self.weights += self.calculate_delta_w(x, expected, Os[j])

                mse_errors[current_epoch] = self.__mid_square_error(Os, self.train_expected_data)

                if (mse_errors[current_epoch] < self.min_error):
                    finished = True

                current_epoch += 1
            
            MSEs_array_train[k] = mse_errors[current_epoch - 1]
        
            print("Finished Training")

            MSEs_array_test[k] = self.test(input_data_sets[k], expected_data_sets[k])
            all_weights = np.append(all_weights, self.weights)

        all_weights = all_weights.reshape((self.k_fold, len(self.weights)))

        # TODO: ver como devolver el mejor

        return MSEs_array_train, MSEs_array_test, all_weights
    
    def test(self, test_input, test_expected_data):
        test_len = len(test_input)
        Os = np.empty(test_len)

        for i in range(test_len):
            h = np.dot(self.weights, test_input[i])
            Os[i] = self.predict(h)
            print(f"Predicted: {self.__denormalize_image(Os[i])}. Expected: {test_expected_data[i]}")

        test_mse = self.__mid_square_error(Os, test_expected_data)
        print(f"Train MSE: {self.train_MSE} \n Test MSE: {self.__mid_square_error(Os, test_expected_data)}")

        print("Finished testing")

        return test_mse
        

    # Funcion de prediccion
    def predict(self, x):
        return self.activation(x)

    # Funciónes de activación O segun el tipo de perceptron
    def activation(self, h):
        switcher = {
            "LINEAR": self.__activate_linear(h),
            "NON_LINEAR_TANH": self.__activate_non_linear_tanh(h),
            "NON_LINEAR_LOG": self.__activate_non_linear_log(h),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")
    
    def __activate_linear(self, h):
        return h
    def __activate_non_linear_tanh(self, h):
        return math.tanh(self.beta * h)
    def __activate_non_linear_log(self, h):
        return 1 / (1 + math.pow(math.e, -2 * self.beta * h))
    
    # Funcion de Δw 
    def calculate_delta_w(self, x, expected, O):
        error = self.__normalize_image(expected) - O
        theta_diff = self.__calculate_theta_diff(O)
        return self.learning_rate * error * theta_diff * x

    # Funcion que calcula θ' segun el tipo de perceptron
    def __calculate_theta_diff(self, O):
        switcher = {
            "LINEAR": self.__calculate_theta_diff_linear(),
            "NON_LINEAR_TANH": self.__calculate_theta_diff_non_linear_tanh(O),
            "NON_LINEAR_LOG": self.__calculate_theta_diff_non_linear_log(O),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __calculate_theta_diff_linear(self):
        return 1
    def __calculate_theta_diff_non_linear_tanh(self, O):
        return self.beta * (1 - O**2)
    def __calculate_theta_diff_non_linear_log(self, O):
        return 2 * self.beta * O * (1 - O)

    # Función de error MSE para finalizar entrenamiento
    def __mid_square_error(self, Os, expected):
        return np.sum((expected - self.__denormalize_image(Os)) ** 2) / len(expected)

    def __calculate_min_and_max(self, expected_data):
        return np.min(expected_data), np.max(expected_data)

    # Funcion que normaliza los resultados segun la imagen de la funcion de activacion
    def __normalize_image(self, values):
        switcher = {
            "LINEAR": self.__normalize_linear_image(values),
            "NON_LINEAR_TANH": self.__normalize_non_linear_tanh_image(values),
            "NON_LINEAR_LOG": self.__normalize_non_linear_log_image(values),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __normalize_linear_image(self, values):
        return values
    # Normalizacion para [a,b] es: X'=((X-Xmin)/(Xmax-Xmin))(b-a)+a
    def __normalize_non_linear_tanh_image(self, values):
        # Image = (-1,1)
        return (2 * (values - self.min) / (self.max - self.min)) - 1
    def __normalize_non_linear_log_image(self, values):
        # Image = (0,1)
        return (values - self.min) / (self.max - self.min)
    
    # Funcion que desnormaliza los resultados segun la imagen de la funcion de activacion
    def __denormalize_image(self, values):
        switcher = {
            "LINEAR": self.__denormalize_linear_image(values),
            "NON_LINEAR_TANH": self.__denormalize_non_linear_tanh_image(values),
            "NON_LINEAR_LOG": self.__denormalize_non_linear_log_image(values),
        }

        return switcher.get(self.perceptron_type, "Tipo de perceptron invalido")

    def __denormalize_linear_image(self, values):
        return values
    def __denormalize_non_linear_tanh_image(self, values):
        return ((values + 1) * (self.max - self.min) * 0.5) + self.min
    def __denormalize_non_linear_log_image(self, values):
        return values * (self.max - self.min) + self.min

    def __str__(self) -> str:
        return f"Perceptron {self.perceptron_type}: {self.weights}" 
    
    def __repr__(self) -> str:
        return self.__str__()