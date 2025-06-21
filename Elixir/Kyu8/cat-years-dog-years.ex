# https://www.codewars.com/kata/cat-years-dog-years

defmodule Dinglemouse do
  @moduledoc false
  defp animal_years(human_years, per_year) do
    cond do
      human_years <= 1 -> 15
      human_years <= 2 -> animal_years(1, per_year) + 9
      true -> animal_years(2, per_year) + (human_years - 2) * per_year
    end
  end

  defp cat_years(human_years) do
    animal_years(human_years, 4)
  end

  defp dog_years(human_years) do
    animal_years(human_years, 5)
  end

  def human_years_cat_years_dog_years(human_years) do
    {human_years, cat_years(human_years), dog_years(human_years)}
  end
end

Dinglemouse.human_years_cat_years_dog_years(1)
Dinglemouse.human_years_cat_years_dog_years(10)
