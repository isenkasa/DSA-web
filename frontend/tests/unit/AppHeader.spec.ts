import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import AppHeader from '@/components/AppHeader.vue'

describe('AppHeader.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'Data Structures and Algorithms'
    const wrapper = shallowMount(AppHeader)
    expect(wrapper.text()).to.include(msg)
  })
})
