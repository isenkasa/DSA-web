import { expect } from 'chai'
import { shallowMount } from '@vue/test-utils'
import MainView from '@/components/MainView.vue'

describe('MainView.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'Welcome to DSA Web Application'
    const wrapper = shallowMount(MainView)
    expect(wrapper.text()).to.include(msg)
  })
})
