import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import App from "./App";
import * as api from "./api";
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("./api");

describe("App component", () => {
  beforeEach(() => {
    vi.clearAllMocks();

    (api.fetchItems as any).mockResolvedValue({
      items: [{ id: 1, name: "Apple", price: 10 }],
    });
    (api.fetchCart as any).mockResolvedValue([
      { id: 1, name: "Apple", qty: 1 },
    ]);
    (api.fetchReport as any).mockResolvedValue({
      total_items_sold: 1,
      total_revenue: 10,
      total_discount_given: 0,
      discount_codes: [],
    });
  });

  it("renders items and cart", async () => {
    render(<App />);

    expect(await screen.findByText("Apple")).toBeInTheDocument();
    expect(screen.getByText("Apple x 1")).toBeInTheDocument();
    expect(screen.getByText("Total Items Sold:")).toBeInTheDocument();
  });

  it("adds item to cart when 'Add to Cart' is clicked", async () => {
    (api.addToCart as any).mockResolvedValue({
      cart: [{ id: 1, name: "Apple", qty: 2 }],
    });

    render(<App />);
    const button = await screen.findByText("Add to Cart");

    fireEvent.click(button);

    await waitFor(() => {
      expect(screen.getByText("Apple x 2")).toBeInTheDocument();
    });
  });

  it("displays message after checkout", async () => {
    (api.checkout as any).mockResolvedValue({
      message: "Order placed",
      total: 100,
    });
    (api.fetchReport as any).mockResolvedValueOnce({
      total_items_sold: 2,
      total_revenue: 110,
      total_discount_given: 10,
      discount_codes: [],
    });

    render(<App />);

    fireEvent.change(await screen.findByPlaceholderText("Discount Code"), {
      target: { value: "DISCOUNT10" },
    });

    fireEvent.click(screen.getByText("Checkout"));

    await waitFor(() =>
      expect(screen.getByText("Order placed. Total: $100")).toBeInTheDocument()
    );
  });
});
