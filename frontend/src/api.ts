import { CartItem, Report } from "./types";

export async function fetchItems(): Promise<any> {
  const res = await fetch(`/items`);
  return res.json();
}

export async function fetchCart(userId: string): Promise<CartItem[]> {
  const res = await fetch(`/cart/${userId}`);
  return res.json();
}

export async function fetchReport(): Promise<Report> {
  const res = await fetch(`/admin/report`);
  return res.json();
}

export async function addToCart(userId: string, item: CartItem) {
  const res = await fetch(`/cart/${userId}/add`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  return res.json();
}

export async function checkout(userId: string, code: string) {
  const res = await fetch(`/checkout/${userId}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ discount_code: code }),
  });
  return res.json();
}
