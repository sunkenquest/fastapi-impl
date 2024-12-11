<template>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-20 sm:gap-10 p-5">
        <template v-if="products.length === 0">
            <div class="col-span-full text-center text-xl text-gray-600">
                No product
            </div>
        </template>
        <template v-else>
            <div v-for="(product, index) in products" :key="index"
                class="w-64 max-w-xs rounded-lg border shadow-md bg-white p-4">
                <img :src="product.image" :alt="product.name" class="w-full h-48 object-cover rounded-lg mb-4" />
                <div class="text-center">
                    <h3 class="text-lg font-semibold text-gray-800">{{ product.name }}</h3>
                    <p class="text-sm text-gray-600 mb-2">{{ product.description }}</p>
                    <p class="text-xl font-bold text-gray-900">${{ product.price.toFixed(2) }}</p>
                    <button @click="addToCart(product)"
                        class="mt-4 w-full dark:bg-gray-900 text-white p-2 rounded-full hover:bg-blue-700 focus:ring-4 focus:ring-blue-300">
                        Add to Cart
                    </button>
                </div>
            </div>
        </template>
    </div>

</template>

<script>
export default {
    data() {
        return {
            products: [
                {
                    id: 1,
                    name: "Product 1",
                    description: "This is the first product.",
                    price: 19.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 2,
                    name: "Product 2",
                    description: "This is the second product.",
                    price: 29.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 3,
                    name: "Product 3",
                    description: "This is the third product.",
                    price: 39.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 4,
                    name: "Product 4",
                    description: "This is the fourth product.",
                    price: 49.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 1,
                    name: "Product 1",
                    description: "This is the first product.",
                    price: 19.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 2,
                    name: "Product 2",
                    description: "This is the second product.",
                    price: 29.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 3,
                    name: "Product 3",
                    description: "This is the third product.",
                    price: 39.99,
                    image: "https://via.placeholder.com/300x200",
                },
                {
                    id: 4,
                    name: "Product 4",
                    description: "This is the fourth product.",
                    price: 49.99,
                    image: "https://via.placeholder.com/300x200",
                },
            ],
        };
    },
    methods: {
        addToCart(product) {
            alert(`Added ${product.name} to the cart!`);
        },
    },
};
</script>
