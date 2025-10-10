"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6

    def test_add_negative_numbers(self): 
        assert add(-1, -1) == -2 
        assert add(-5, 3) == -2 
    def test_subtract_negative_numbers(self): 
        assert subtract(-1, -1) == 0 
        assert subtract(-5, -3) == -2

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)

# TODO: Students will add TestMultiplyDivide class

class TestPowerSqrt:
    """Test power and sqrt functions with validation and edge cases"""

    def test_power_positive_numbers(self):
        """Test raising a number to a positive power"""
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_power_negative_and_fractional(self):
        """Test power with negative and fractional exponents"""
        assert power(2, -1) == 0.5
        assert pytest.approx(power(9, 0.5)) == 3.0  # sqrt via power

    def test_power_input_validation(self):
        """Test power rejects non-numeric inputs"""
        with pytest.raises(TypeError, match="Power requires numeric inputs"):
            power("2", 3)
        with pytest.raises(TypeError, match="Power requires numeric inputs"):
            power(2, "3")

    def test_sqrt_positive_numbers(self):
        """Test sqrt with positive inputs"""
        assert sqrt(25) == 5
        assert pytest.approx(sqrt(2)) == 1.4142135623

    def test_sqrt_zero(self):
        """Test sqrt with zero input"""
        assert sqrt(0) == 0

    def test_sqrt_negative_numbers(self):
        """Test sqrt rejects negative inputs"""
        with pytest.raises(ValueError, match="Cannot take square root of negative number"):
            sqrt(-9)

    def test_sqrt_input_validation(self):
        """Test sqrt rejects non-numeric inputs"""
        with pytest.raises(TypeError, match="Sqrt requires numeric input"):
            sqrt("16")