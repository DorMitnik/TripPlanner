import { render, screen, fireEvent } from '@testing-library/react';
import Register from '../components/Register';

test('renders register form', () => {
  render(<Register />);
  expect(screen.getByLabelText(/username/i)).toBeInTheDocument();
  expect(screen.getByLabelText(/password/i)).toBeInTheDocument();
  expect(screen.getByRole('button', { name: /register/i })).toBeInTheDocument();
});
