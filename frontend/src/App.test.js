import { render, screen } from '@testing-library/react';
import App from './App';
import { BrowserRouter } from 'react-router-dom';
import axios from 'axios';

test('renders the welcome message', async () => {
  jest.spyOn(axios, 'get').mockImplementation((url) =>
    Promise.resolve({
      data: {
        status: 'success',
        data: url.includes('/api/order/') ? [{ id: 1 }] : [],
      },
    })
  );

  render(<App />, { wrapper: BrowserRouter });
  expect(screen.getByText(/Welcome/i)).toBeInTheDocument();
  expect(await screen.findByText('Cart: 1')).toBeInTheDocument();
});
