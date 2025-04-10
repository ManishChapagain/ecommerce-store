export type CartItem = {
  id: number;
  name: string;
  price: number;
  qty: number;
};

export type DiscountCode = {
  code: string;
  used: boolean;
};

export type Report = {
  total_items_sold: number;
  total_revenue: number;
  total_discount_given: number;
  discount_codes: DiscountCode[];
};
