from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(
        max_length=255, unique=True
        )
    slug = models.SlugField(
        max_length=255, unique=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    # General Info
    name = models.CharField(
        max_length=255, unique=True
    )
    slug = models.SlugField(
        max_length=255, unique=True,
        blank=True
    )
    description = models.TextField(
        blank=True, help_text="Detailed product description"
    )
    
    # Category and Tagging
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL,
        null=True, related_name="products"
    )
    tags = models.ManyToManyField(
        "Tag", blank=True, related_name="products"
    )

    # Pricing and Stock
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    discount_price = models.DecimalField(
        max_digits=10, decimal_places=2,
        null=True, blank=True,
        help_text="Leave blank if no discount"
    )
    stock = models.PositiveIntegerField(
        default=0, help_text="Number of items in stock"
    )
    is_active = models.BooleanField(
        default=True, help_text="Set to false if the product is unavailable"
    )

    # Media
    image = models.ImageField(
        upload_to="products/images/",
        blank=True, null=True
    )
    additional_images = models.ManyToManyField(
        "ProductImage", blank=True, related_name="products"
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Product"
        verbose_name_plural = "Products"

class ProductImage(models.Model):
    image = models.ImageField(upload_to="products/additional_images/")
    alt_text = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.image}"

class Tag(models.Model):
    name = models.CharField(
        max_length=50, unique=True
    )
    slug = models.SlugField(
        max_length=50, unique=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
