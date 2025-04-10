import { fetchItems, fetchCart, fetchReport, addToCart, checkout } from "./api";
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.stubGlobal("fetch", vi.fn());

describe("API functions", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("fetchItems returns item list", async () => {
    (fetch as any).mockResolvedValueOnce({
      json: () =>
        Promise.resolve({
          items: [{ id: 1, name: "Apple", price: 10 }],
        }),
    });

    const result = await fetchItems();
    expect(result.items[0].id).toBe(1);
    expect(result.items[0].name).toBe("Apple");
    expect(result.items[0].price).toBe(10);
  });

  it("fetchCart returns cart items", async () => {
    (fetch as any).mockResolvedValueOnce({
      json: () => Promise.resolve([{ id: 2, name: "Banana", qty: 5 }]),
    });

    const result = await fetchCart("1");
    expect(result[0].id).toBe(2);
    expect(result[0].name).toBe("Banana");
    expect(result[0].qty).toBe(5);
  });

  it("fetchReport returns report", async () => {
    (fetch as any).mockResolvedValueOnce({
      json: () =>
        Promise.resolve({
          total_items_sold: 10,
          total_revenue: 50,
          total_discount_given: 5,
          discount_codes: [{ code: "A3N6QA", used: true }],
        }),
    });

    const result = await fetchReport();
    expect(result.total_items_sold).toBe(10);
    expect(result.total_revenue).toBe(50);
    expect(result.total_discount_given).toBe(5);
    expect(result.discount_codes[0].used).toBe(true);
  });

  it("addToCart sends item and returns updated cart", async () => {
    (fetch as any).mockResolvedValueOnce({
      json: () =>
        Promise.resolve({
          cart: [{ id: 1, name: "Apple", qty: 1 }],
        }),
    });

    const result = await addToCart("1", {
      id: 1,
      name: "Apple",
      price: 10,
      qty: 1,
    });
    expect(result.cart[0].name).toBe("Apple");
  });

  it("checkout sends discount code and returns total", async () => {
    (fetch as any).mockResolvedValueOnce({
      json: () => Promise.resolve({ message: "Order placed", total: 100 }),
    });

    const result = await checkout("1", "CODE123");
    expect(result.total).toBe(100);
  });
});
